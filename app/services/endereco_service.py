from app.database import get_connection, get_cursor
from app.schemas.endereco_schema import EnderecoCreate, EnderecoUpdate


def criar_endereco(dados: EnderecoCreate):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            """
            INSERT INTO endereco (id_usuario, rua, numero, bairro, cidade, estado, cep)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING *
            """,
            (dados.id_usuario, dados.rua, dados.numero,
             dados.bairro, dados.cidade, dados.estado, dados.cep),
        )
        novo = cur.fetchone()
        conn.commit()
        return novo
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


def listar_enderecos():
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute("SELECT * FROM endereco")
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()


def enderecos_por_usuario(id_usuario: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute("SELECT * FROM endereco WHERE id_usuario = %s", (id_usuario,))
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()


def buscar_endereco(id_endereco: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute("SELECT * FROM endereco WHERE id_endereco = %s", (id_endereco,))
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()


def atualizar_endereco(id_endereco: int, dados: EnderecoUpdate):
    campos = {k: v for k, v in dados.model_dump().items() if v is not None}
    if not campos:
        return None

    set_clause = ", ".join(f"{col} = %s" for col in campos)
    valores = list(campos.values()) + [id_endereco]

    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            f"UPDATE endereco SET {set_clause} WHERE id_endereco = %s RETURNING *",
            valores,
        )
        atualizado = cur.fetchone()
        conn.commit()
        return atualizado
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


def deletar_endereco(id_endereco: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            "DELETE FROM endereco WHERE id_endereco = %s RETURNING id_endereco",
            (id_endereco,),
        )
        deletado = cur.fetchone()
        conn.commit()
        return deletado
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()