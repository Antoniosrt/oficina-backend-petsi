from app.database import get_connection
from psycopg2.extras import RealDictCursor

def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM produto WHERE ativo = TRUE")
    produtos = cursor.fetchall() 
    cursor.close()
    conn.close()
    return produtos

def criar(info):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("""
                   INSERT INTO produto(id_categoria, nome, descricao, preco, estoque, imagem_url, ativo)
                   VALUES(%s, %s, %s, %s, %s, %s, %s)
                   RETURNING *
                   """,(info.id_categoria, info.nome, info.descricao, info.preco,info.estoque,info.imagem_url,info.ativo))
    novo = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return novo

def atualizar(id_produto: int, info):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        UPDATE produto
        SET id_categoria = %s, nome = %s,descricao=%s, preco = %s, estoque = %s, imagem_url = %s, ativo = %s
        WHERE id_produto = %s
        RETURNING *
""",(info.id_categoria, info.nome, info.descricao, info.preco, info.estoque, info.imagem_url, info.ativo, id_produto))
    atualizado = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return atualizado

def deletar(id_produto: int)->bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("Update produto SET ativo = FALSE where id_produto = %s", (id_produto,))

    afetadas = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return afetadas > 0