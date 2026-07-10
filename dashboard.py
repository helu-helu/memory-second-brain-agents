import os
import streamlit as st
import requests
import json
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# Cấu hình API Server
API_BASE = "http://127.0.0.1:8001"
API_KEY = os.environ.get("APP_API_KEY", "my-super-secret-key-123")
HEADERS = {"X-API-Key": API_KEY}

st.set_page_config(page_title="Second Brain Dashboard", page_icon=":material/memory:", layout="wide")

st.title(":material/memory: Second Brain Dashboard")
st.markdown("Quản trị dữ liệu RAG và Ký ức đa tác vụ (Multi-Agent Memory) của hệ thống.")

tab1, tab2 = st.tabs(["🧩 RAG (Knowledge Base)", "🧠 Memory (Mem0)"])

with tab1:
    st.header("Truy vấn Kho Tri Thức (RAG)")
    
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            rag_query = st.text_input("Nhập câu hỏi để tìm kiếm trong RAG...", placeholder="Ví dụ: Làm sao để cài đặt cơ sở dữ liệu?")
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            search_rag_btn = st.button(":material/search: Tìm kiếm RAG")
            
        if search_rag_btn and rag_query:
            with st.spinner("Đang tìm kiếm..."):
                try:
                    res = requests.get(f"{API_BASE}/rag/search", params={"q": rag_query}, headers=HEADERS)
                    if res.status_code == 200:
                        data = res.json().get("result", "")
                        st.markdown("**Kết quả:**")
                        st.info(data)
                    else:
                        st.error(f"Lỗi: {res.text}")
                except Exception as e:
                    st.error(f"Không thể kết nối đến API Server: {e}")

with tab2:
    st.header("Quản trị Ký Ức (Multi-Agent)")
    
    agent_id = st.text_input("Agent ID", value="default_user", help="Nhập ID của Agent để xem các ký ức riêng biệt.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        with st.container(border=True):
            st.subheader(":material/search: Tìm kiếm Ký ức")
            search_mem = st.text_input("Tìm kiếm:", placeholder="Ví dụ: tôi thích gì?")
            if st.button(":material/search: Tìm Ký ức"):
                if search_mem:
                    with st.spinner("Đang tìm..."):
                        try:
                            res = requests.get(f"{API_BASE}/memory/search", params={"q": search_mem, "agent_id": agent_id}, headers=HEADERS)
                            if res.status_code == 200:
                                st.markdown("**Kết quả:**")
                                st.info(res.json().get("result", ""))
                            else:
                                st.error("Lỗi khi tìm kiếm.")
                        except Exception as e:
                            st.error(f"Lỗi kết nối: {e}")
                            
        with st.container(border=True):
            st.subheader(":material/add: Thêm ký ức mới")
            new_memory = st.text_area("Nội dung ký ức (Lưu ý: Đây là để THÊM mới, không phải để tìm kiếm):")
            if st.button(":material/save: Thêm Ký Ức"):
                if new_memory:
                    with st.spinner("Đang thêm..."):
                        try:
                            res = requests.post(f"{API_BASE}/memory/add", json={"text": new_memory, "agent_id": agent_id}, headers=HEADERS)
                            if res.status_code == 200:
                                st.success("Đã thêm thành công!")
                            else:
                                st.error("Lỗi khi thêm ký ức.")
                        except Exception as e:
                            st.error(f"Lỗi kết nối: {e}")
                else:
                    st.warning("Vui lòng nhập nội dung.")
                    
    with col2:
        with st.container(border=True):
            st.subheader(":material/list: Danh sách Ký ức hiện tại")
            if st.button(":material/refresh: Làm mới danh sách"):
                pass # Sẽ tự động gọi lại code dưới
            
            try:
                res = requests.get(f"{API_BASE}/memory/all", params={"agent_id": agent_id}, headers=HEADERS)
                if res.status_code == 200:
                    memories = res.json().get("memories", [])
                    if not memories:
                        st.info("Chưa có ký ức nào cho Agent này.")
                    else:
                        for m in memories:
                            with st.expander(f":material/bolt: {m.get('memory', m.get('fact', 'Memory'))}"):
                                st.json(m)
                else:
                    st.error("Lỗi khi tải danh sách ký ức.")
            except Exception as e:
                st.error("Không thể kết nối đến API Server.")
