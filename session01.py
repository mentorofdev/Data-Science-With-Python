import streamlit as st
import yfinance as yf

st.write("""
# Demo giá chính khoán
  Hiển thị dữ liệu chính khoán **closing price** and ***volume*** của Google!
""")

#Khai báo mã chính khoán mà mình cần lấy để phân tích
# AAPLE, GOOGLE  VÀ RẤT NHIỀU MÃ KHÁC NỮA.

tickerSymbol = 'GOOGL'

# lấy dữ liệu chính khoán của GOOGLE

tickerData = yf.Ticker(tickerSymbol)

# Lấy giá chính khoán từ 2019-5-31 đến 2021-8-20 của mã GOOGLE

tickerDf = tickerData.history(period='1d', start='2019-5-31', end='2021-8-20')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)

"""
    OK MỌI THỨ ĐÃ XONG GIỜ THÌ MÌNH CHẠY XEM THỬ . SỬ DỤNG streamlit để Demo chart . 
 
     streamlit run session01.py 
     Sau khi chạy lệnh trên thì sẽ mở trình duyệt 
 
    Local URL: http://localhost:8501
    
    Ok bài này mình tạm dừng ở đây hy vọng các bạn có cái nhìn tổng quan về sức mạnh của python trong việc xử lý dữ liệu 

"""