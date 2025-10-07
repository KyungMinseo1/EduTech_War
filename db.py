# db.py
import psycopg2
import streamlit as st

@st.cache_resource
def init_connection():
    """Neon DB 연결"""
    try:
        conn = psycopg2.connect(**st.secrets["postgres"])
        return conn
    except Exception as e:
        st.error(f"연결 실패: {e}")
        return None

# 테이블 생성용 함수
def init_tables(conn):
    try:
        with conn.cursor() as cur:
            # diary 테이블: name UNIQUE 적용
            cur.execute("""
                CREATE TABLE IF NOT EXISTS diary (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE,
                    content1 TEXT,
                    content2 TEXT,
                    content3 TEXT,
                    created_at TIMESTAMP DEFAULT NOW()
                );
            """)
            
            # quiz 테이블: name UNIQUE 적용
            cur.execute("""
                CREATE TABLE IF NOT EXISTS quiz (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE,
                    q1 BOOL,
                    q2 BOOL,
                    q3 BOOL,
                    q4 BOOL,
                    q5 BOOL,
                    q6 BOOL,
                    q7 BOOL,
                    q8 BOOL,
                    q9 BOOL,
                    created_at TIMESTAMP DEFAULT NOW()
                );
            """)
            conn.commit()
        st.cache_data.clear()
    except Exception as e:
        st.error(f"오류: {e}")
