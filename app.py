# import streamlit as st
# import requests

# st.title("💻 Streamlit + FastAPI Demo")

# name = st.text_input("Item Name")
# price = st.number_input("Price", min_value=0.0)
# quantity = st.number_input("Quantity", min_value=0)

# if st.button("Calculate Total"):
#     payload = {"name": name, "price": price, "quantity": quantity}
#     response = requests.post("http://127.0.0.1:8000/items/", json=payload)
    
#     if response.status_code == 200:
#         data = response.json()
#         st.success(f"Total cost for {data['name']}: ₹{data['total_cost']}")
#     else:
#         st.error("Error calling API")


# import streamlit as st
# import requests

# st.title("Calculator")

# n1 = st.number_input("Enter 1st Number : ")
# n2 = st.number_input("Enter 2nd Number : ")

# if st.button("Add"):
#     response = requests.get("http://127.0.0.1:8000/sum/", params={"a":n1, "b":n2})
#     print(response.status_code)
#     if response.status_code == 200:
#         result = response.json()
#         st.success("Result :" + str({result["sum"]}))
#     else:
#         st.error("Error Occured")


# if st.button("Subtract"):
#     response = requests.get("http://127.0.0.1:8000/sub/", params={"a":n1, "b":n2})
#     print(response.status_code)
#     if response.status_code == 200:
#         result = response.json()
#         st.success("Result :" + str({result["sum"]}))
#     else:
#         st.error("Error Occured")



# if st.button("Multiply"):
#     response = requests.get("http://127.0.0.1:8000/mult/", params={"a":n1, "b":n2})
#     print(response.status_code)
#     if response.status_code == 200:
#         result = response.json()
#         st.success("Result :" + str({result["sum"]}))
#     else:
#         st.error("Error Occured")


# if st.button("Division"):
#     response = requests.get("http://127.0.0.1:8000/div/", params={"a":n1, "b":n2})
#     print(response.status_code)
#     if response.status_code == 200:
#         result = response.json()
#         st.success("Result :" + str({result["sum"]}))
#     else:
#         st.error("Error Occured")


import streamlit as st
import requests

st.title("FastAPI + Streamlit Calculator")

n1 = st.number_input("Enter 1st Number : ", value=0)
n2 = st.number_input("Enter 2nd Number : ", value=0)

if st.button("Add"):
    response = requests.post("http://127.0.0.1:8000/sum/", json={"a": n1, "b": n2})
    st.success(response.json())

if st.button("Subtract"):
    response = requests.get("http://127.0.0.1:8000/subtract/", params={"a": n1, "b": n2})
    st.success(response.json())

if st.button("Multiply"):
    response = requests.get("http://127.0.0.1:8000/multiply/", params={"a": n1, "b": n2})
    st.success(response.json())

if st.button("Divide"):
    response = requests.get("http://127.0.0.1:8000/divide/", params={"a": n1, "b": n2})
    if response.status_code == 200:
        st.success(response.json())
    else:
        st.error(response.json()["detail"])


