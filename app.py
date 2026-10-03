import os
import json
import base64
import streamlit as st
from PIL import Image

# ---------------------------------------------------------
# PAGE CONFIGURATION & CUSTOM DARK THEME CSS
# ---------------------------------------------------------
st.set_page_config(
    page_title="VETERAN ONLINE STORE",
    page_icon="👕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

CUSTOM_CSS = """
<style>
    /* Dark Theme Base Styling */
    .stApp {
        background-color: #0d0d0e;
        color: #e0e0e0;
    }
    
    /* Top Header Bar Styling (Inspired by Reference UI) */
    .nav-bar {
        background-color: rgba(25, 25, 28, 0.85);
        border: 1px solid #2a2a2e;
        border-radius: 12px;
        padding: 12px 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
    }
    
    .nav-title {
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 24px;
        font-weight: 800;
        letter-spacing: 2px;
        color: #ffffff;
        margin: 0;
    }

    /* Hero Banner Section */
    .hero-container {
        background: linear-gradient(180deg, rgba(20,20,22,0.6) 0%, rgba(13,13,14,1) 100%), 
                    url('https://images.unsplash.com/photo-1556905055-8f358a7a47b2?q=80&w=1200&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        border-radius: 16px;
        padding: 50px 30px;
        border: 1px solid #26262a;
        margin-bottom: 30px;
        text-align: left;
    }

    .hero-badge {
        background-color: #e63946;
        color: white;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        padding: 4px 10px;
        border-radius: 20px;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 12px;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 900;
        letter-spacing: 1px;
        color: #ffffff;
        margin-bottom: 10px;
    }

    /* Card Layout for Products */
    .product-card {
        background-color: #161619;
        border: 1px solid #28282d;
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 20px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .product-card:hover {
        border-color: #e63946;
        transform: translateY(-2px);
    }

    .product-category {
        color: #e63946;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .product-title {
        font-size: 18px;
        font-weight: 700;
        color: #ffffff;
        margin: 4px 0;
    }

    .product-price {
        font-size: 20px;
        font-weight: 800;
        color: #2ecc71;
        margin-bottom: 8px;
    }

    /* Streamlit Button Overrides */
    div.stButton > button {
        border-radius: 20px !important;
        background-color: #222226 !important;
        color: #ffffff !important;
        border: 1px solid #38383e !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }

    div.stButton > button:hover {
        background-color: #e63946 !important;
        border-color: #e63946 !important;
        color: #ffffff !important;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------------------------------------------------
# DATA PERSISTENCE & INITIALIZATION
# ---------------------------------------------------------
DATA_FILE = "products.json"
IMAGE_DIR = "product_images"

if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

DEFAULT_PRODUCTS = [
    {"id": 1, "name": "Veteran Tactical Hoodie", "category": "Hoodie", "price": 55.00, "description": "Premium heavy cotton blend hoodie.", "image": ""},
    {"id": 2, "name": "Pro Fitness Shorts", "category": "Shorts", "price": 30.00, "description": "Lightweight breathable gym shorts.", "image": ""},
    {"id": 3, "name": "Classic Veteran T-Shirt", "category": "T-shirt", "price": 25.00, "description": "100% Ring-spun cotton soft tee.", "image": ""},
    {"id": 4, "name": "Urban Sweat Pants", "category": "Sweat pants", "price": 45.00, "description": "Comfortable tailored fleece sweatpants.", "image": ""},
    {"id": 5, "name": "Heavyweight Sweatshirt", "category": "Sweat shirts", "price": 50.00, "description": "Cozy pullover crewneck sweatshirt.", "image": ""},
    {"id": 6, "name": "Winter Tactical Ski Mask", "category": "Ski mask", "price": 20.00, "description": "Windproof thermal balaclava.", "image": ""}
]

def load_products():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return DEFAULT_PRODUCTS
    else:
        save_products(DEFAULT_PRODUCTS)
        return DEFAULT_PRODUCTS

def save_products(products):
    with open(DATA_FILE, "w") as f:
        json.dump(products, f, indent=4)

if "products" not in st.session_state:
    st.session_state.products = load_products()

if "cart" not in st.session_state:
    st.session_state.cart = []

# ---------------------------------------------------------
# HEADER / NAVIGATION BAR
# ---------------------------------------------------------
st.markdown("""
<div class="nav-bar">
    <div class="nav-title">VETERAN ONLINE STORE</div>
</div>
""", unsafe_allow_html=True)

# Navigation Tabs
mode = st.radio(
    "Navigate", 
    options=["🏪 Storefront", "🛒 Shopping Cart", "⚙️ Owner Dashboard"], 
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<hr style='border: 1px solid #222225; margin-bottom: 25px;'>", unsafe_allow_html=True)

# ---------------------------------------------------------
# MODE 1: STOREFRONT
# ---------------------------------------------------------
if mode == "🏪 Storefront":
    # Hero Banner
    st.markdown("""
    <div class="hero-container">
        <span class="hero-badge">OFFICIAL STORE</span>
        <div class="hero-title">VETERAN APPAREL COLLECTION</div>
        <p style="color: #b0b0b5; max-width: 600px;">
            Explore top-tier streetwear and apparel crafted for comfort, tactical style, and durability.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Category Filter
    categories = ["All", "Hoodie", "Shorts", "T-shirt", "Sweat pants", "Sweat shirts", "Ski mask"]
    selected_cat = st.selectbox("Filter by Category", categories)

    # Filter Items
    if selected_cat == "All":
        filtered_items = st.session_state.products
    else:
        filtered_items = [p for p in st.session_state.products if p["category"] == selected_cat]

    if not filtered_items:
        st.info("No items found in this category.")
    else:
        # Render product grid (3 columns)
        cols = st.columns(3)
        for idx, prod in enumerate(filtered_items):
            col = cols[idx % 3]
            with col:
                st.markdown(f"""
                <div class="product-card">
                    <span class="product-category">{prod['category']}</span>
                    <div class="product-title">{prod['name']}</div>
                    <div class="product-price">${prod['price']:.2f}</div>
                    <p style="color: #888; font-size: 13px;">{prod.get('description', '')}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Display image if available
                if prod.get("image") and os.path.exists(prod["image"]):
                    st.image(prod["image"], use_column_width=True)
                else:
                    st.caption("📷 Image placeholder")

                if st.button(f"Add to Cart 🛒", key=f"add_{prod['id']}"):
                    st.session_state.cart.append(prod)
                    st.toast(f"Added {prod['name']} to cart!", icon="✅")

# ---------------------------------------------------------
# MODE 2: SHOPPING CART
# ---------------------------------------------------------
elif mode == "🛒 Shopping Cart":
    st.header("Your Shopping Cart")
    if not st.session_state.cart:
        st.info("Your cart is empty. Return to the storefront to add items!")
    else:
        total = sum(item["price"] for item in st.session_state.cart)
        
        for idx, item in enumerate(st.session_state.cart):
            c1, c2, c3 = st.columns([3, 1, 1])
            with c1:
                st.write(f"**{item['name']}** ({item['category']})")
            with c2:
                st.write(f"${item['price']:.2f}")
            with c3:
                if st.button("Remove", key=f"cart_rem_{idx}"):
                    st.session_state.cart.pop(idx)
                    st.rerun()

        st.markdown("---")
        st.subheader(f"Total Amount: **${total:.2f}**")
        
        if st.button("Proceed to Checkout", type="primary"):
            st.success("Thank you for your order! Jason will process it shortly.")
            st.session_state.cart = []

# ---------------------------------------------------------
# MODE 3: OWNER DASHBOARD (ADMIN CONTROLS)
# ---------------------------------------------------------
elif mode == "⚙️ Owner Dashboard":
    st.header("⚙️ Owner Management Portal")
    st.caption("Manage items, upload new clothing images, edit prices, or remove products.")

    tab1, tab2 = st.tabs(["➕ Upload New Item", "✏️ Edit & Delete Items"])

    # TAB 1: ADD NEW CLOTHING ITEM
    with tab1:
        st.subheader("Add New Apparel to Store")
        with st.form("add_product_form", clear_on_submit=True):
            new_name = st.text_input("Item Name")
            new_cat = st.selectbox("Category", ["Hoodie", "Shorts", "T-shirt", "Sweat pants", "Sweat shirts", "Ski mask"])
            new_price = st.number_input("Price ($)", min_value=0.0, step=1.00, value=25.00)
            new_desc = st.text_area("Description")
            uploaded_file = st.file_uploader("Upload Image from Media", type=["png", "jpg", "jpeg", "webp"])

            submitted = st.form_submit_button("Upload & Save Product")
            
            if submitted:
                if not new_name:
                    st.error("Please enter an item name.")
                else:
                    img_path = ""
                    if uploaded_file is not None:
                        img_path = os.path.join(IMAGE_DIR, f"{int(os.urandom(4).hex(), 16)}_{uploaded_file.name}")
                        image = Image.open(uploaded_file)
                        image.save(img_path)

                    new_id = max([p["id"] for p in st.session_state.products], default=0) + 1
                    new_item = {
                        "id": new_id,
                        "name": new_name,
                        "category": new_cat,
                        "price": float(new_price),
                        "description": new_desc,
                        "image": img_path
                    }

                    st.session_state.products.append(new_item)
                    save_products(st.session_state.products)
                    st.success(f"Successfully added '{new_name}' to the catalog!")

    # TAB 2: EDIT & DELETE EXISTING ITEMS
    with tab2:
        st.subheader("Manage Catalog")
        if not st.session_state.products:
            st.write("No products available to edit.")
        else:
            for idx, prod in enumerate(st.session_state.products):
                with st.expander(f"📦 {prod['name']} (${prod['price']:.2f}) - {prod['category']}"):
                    col_a, col_b = st.columns([2, 1])
                    
                    with col_a:
                        updated_name = st.text_input("Item Name", prod["name"], key=f"edit_name_{prod['id']}")
                        updated_cat = st.selectbox("Category", ["Hoodie", "Shorts", "T-shirt", "Sweat pants", "Sweat shirts", "Ski mask"], index=["Hoodie", "Shorts", "T-shirt", "Sweat pants", "Sweat shirts", "Ski mask"].index(prod["category"]) if prod["category"] in ["Hoodie", "Shorts", "T-shirt", "Sweat pants", "Sweat shirts", "Ski mask"] else 0, key=f"edit_cat_{prod['id']}")
                        updated_price = st.number_input("Price ($)", min_value=0.0, value=float(prod["price"]), step=1.00, key=f"edit_price_{prod['id']}")
                        updated_desc = st.text_area("Description", prod.get("description", ""), key=f"edit_desc_{prod['id']}")
                        
                        btn1, btn2 = st.columns(2)
                        with btn1:
                            if st.button("Save Changes", key=f"save_{prod['id']}"):
                                prod["name"] = updated_name
                                prod["category"] = updated_cat
                                prod["price"] = float(updated_price)
                                prod["description"] = updated_desc
                                save_products(st.session_state.products)
                                st.success("Updated successfully!")
                                st.rerun()

                        with btn2:
                            if st.button("Delete Item", key=f"del_{prod['id']}"):
                                st.session_state.products.pop(idx)
                                save_products(st.session_state.products)
                                st.warning("Item deleted!")
                                st.rerun()

                    with col_b:
                        if prod.get("image") and os.path.exists(prod["image"]):
                            st.image(prod["image"], caption="Current Image", use_column_width=True)
                        else:
                            st.info("No image attached.")
