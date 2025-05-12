import streamlit as st
from datetime import datetime

def main():
    st.title("📋 Toolbox Talk 회의록")

    with st.form("meeting_form"):
        st.subheader("1️⃣ 회의 정보")
        col1, col2 = st.columns(2)
        with col1:
            date = st.date_input("날짜", value=datetime.now())
            location = st.text_input("장소", "현장 A")
        with col2:
            time = st.time_input("시간", value=datetime.now().time())
            task = st.text_input("작업 내용", "고소작업")

        st.subheader("2️⃣ 참석자 명단")
        attendees = st.text_area("참석자 (쉼표로 구분)", placeholder="김작업, 박엔지니어, 이안전")

        st.subheader("3️⃣ 논의 내용")
        risk = st.text_input("위험요소")
        measure = st.text_input("안전대책")

        st.subheader("4️⃣ 결정사항 및 조치")
        action = st.text_area("조치 내용 및 담당자")

        st.subheader("5️⃣ 회의록 확인 및 서명")
        confirmed_by = st.text_input("확인자 이름")
        confirm = st.checkbox("위 내용을 확인합니다.")

        submitted = st.form_submit_button("저장")
        if submitted and confirm:
            st.success("회의록이 저장되었습니다.")
            st.write("### 회의 요약")
            st.write(f"🗓 날짜: {date} / ⏰ 시간: {time}")
            st.write(f"📍 장소: {location} / 작업: {task}")
            st.write(f"👥 참석자: {attendees}")
            st.write(f"⚠️ 위험요소: {risk} → ✅ 안전대책: {measure}")
            st.write(f"📌 결정 및 조치사항: {action}")
            st.write(f"✍️ 확인자: {confirmed_by} (확인 완료)")

if __name__ == "__main__":
    main()