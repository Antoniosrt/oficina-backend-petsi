from app.database import get_connection, get_cursor
from app.schemas.categoria_schema import CategoriaCreate, CategoriaUpdate


def criar_categoria(dados: CategoriaCreate):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            "INSERT INTO categoria (nome, descricao) VALUES (%s, %s) RETURNING *",
            (dados.nome, dados.descricao),
        )
        nova = cur.fetchone()
        conn.commit()
        return nova
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


def listar_categorias():
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute("SELECT * FROM categoria")
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()


def buscar_categoria(id_categoria: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute("SELECT * FROM categoria WHERE id_categoria = %s", (id_categoria,))
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()


def atualizar_categoria(id_categoria: int, dados: CategoriaUpdate):
    campos = {k: v for k, v in dados.model_dump().items() if v is not None}
    if not campos:
        return None

    set_clause = ", ".join(f"{col} = %s" for col in campos)
    valores = list(campos.values()) + [id_categoria]

    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            f"UPDATE categoria SET {set_clause} WHERE id_categoria = %s RETURNING *",
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


def deletar_categoria(id_categoria: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            "DELETE FROM categoria WHERE id_categoria = %s RETURNING id_categoria",
            (id_categoria,),
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