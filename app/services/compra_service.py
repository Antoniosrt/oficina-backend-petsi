from app.database import get_connection, get_cursor
from app.schemas.compra_schema import CompraCreate, CompraUpdate


def criar_compra(dados: CompraCreate):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            """
            INSERT INTO compra (id_usuario, status, valor_total)
            VALUES (%s, %s, %s)
            RETURNING *
            """,
            (dados.id_usuario, dados.status, dados.valor_total),
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


def listar_compras():
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute("SELECT * FROM compra")
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()


def compras_por_usuario(id_usuario: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute("SELECT * FROM compra WHERE id_usuario = %s", (id_usuario,))
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()


def buscar_compra(id_compra: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute("SELECT * FROM compra WHERE id_compra = %s", (id_compra,))
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()


def atualizar_compra(id_compra: int, dados: CompraUpdate):
    campos = {k: v for k, v in dados.model_dump().items() if v is not None}
    if not campos:
        return None

    set_clause = ", ".join(f"{col} = %s" for col in campos)
    valores = list(campos.values()) + [id_compra]

    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            f"UPDATE compra SET {set_clause} WHERE id_compra = %s RETURNING *",
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


def deletar_compra(id_compra: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            "DELETE FROM compra WHERE id_compra = %s RETURNING id_compra",
            (id_compra,),
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