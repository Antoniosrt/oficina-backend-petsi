from app.database import get_connection, get_cursor
from app.schemas.item_compra_schema import ItemCompraCreate, ItemCompraUpdate


def criar_item(dados: ItemCompraCreate):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            """
            INSERT INTO item_compra (id_compra, id_produto, quantidade, preco_unitario, subtotal)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING *
            """,
            (dados.id_compra, dados.id_produto, dados.quantidade,
             dados.preco_unitario, dados.subtotal),
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


def listar_itens():
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute("SELECT * FROM item_compra")
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()


def itens_por_compra(id_compra: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute("SELECT * FROM item_compra WHERE id_compra = %s", (id_compra,))
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()


def buscar_item(id_item_compra: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute("SELECT * FROM item_compra WHERE id_item_compra = %s", (id_item_compra,))
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()


def atualizar_item(id_item_compra: int, dados: ItemCompraUpdate):
    campos = {k: v for k, v in dados.model_dump().items() if v is not None}
    if not campos:
        return None

    set_clause = ", ".join(f"{col} = %s" for col in campos)
    valores = list(campos.values()) + [id_item_compra]

    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            f"UPDATE item_compra SET {set_clause} WHERE id_item_compra = %s RETURNING *",
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


def deletar_item(id_item_compra: int):
    conn = get_connection()
    cur = get_cursor(conn)
    try:
        cur.execute(
            "DELETE FROM item_compra WHERE id_item_compra = %s RETURNING id_item_compra",
            (id_item_compra,),
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