from app.database import get_connection, get_cursor
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate


def criar_usuario(dados: UsuarioCreate):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            """
            INSERT INTO usuario (nome, email, senha, telefone)
            VALUES (%s, %s, %s, %s)
            RETURNING id_usuario, nome, email, telefone, data_cadastro
            """,
            (dados.nome, dados.email, dados.senha, dados.telefone),
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


def listar_usuarios():
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute("SELECT id_usuario, nome, email, telefone, data_cadastro FROM usuario")
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()


def buscar_usuario(id_usuario: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            "SELECT id_usuario, nome, email, telefone, data_cadastro FROM usuario WHERE id_usuario = %s",
            (id_usuario,),
        )
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()


def atualizar_usuario(id_usuario: int, dados: UsuarioUpdate):
    campos = {k: v for k, v in dados.model_dump().items() if v is not None}
    if not campos:
        return None

    set_clause = ", ".join(f"{col} = %s" for col in campos)
    valores = list(campos.values()) + [id_usuario]

    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            f"""
            UPDATE usuario SET {set_clause}
            WHERE id_usuario = %s
            RETURNING id_usuario, nome, email, telefone, data_cadastro
            """,
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


def deletar_usuario(id_usuario: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            "DELETE FROM usuario WHERE id_usuario = %s RETURNING id_usuario",
            (id_usuario,),
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