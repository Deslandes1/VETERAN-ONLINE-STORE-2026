# 👕 VETERAN ONLINE STORE

A modern, dark-themed e-commerce web application built in Python using **Streamlit**. Designed specifically for clothing brands and apparel stores, **VETERAN ONLINE STORE** provides a seamless storefront experience for customers and an easy-to-use administration dashboard for managing inventory.

---

## 🌟 Key Features

### 🏪 Storefront (Customer Experience)
* **Sleek Dark Theme**: Modern UI inspired by contemporary streetwear digital storefronts.
* **Category Filtering**: Quick filter options for:
  * Hoodie
  * Shorts
  * T-shirt
  * Sweat pants
  * Sweat shirts
  * Ski mask
* **Interactive Cart System**: Add items to your cart with instant feedback notifications and calculated totals.

### ⚙️ Owner Dashboard (Inventory Management)
* **Media Uploads**: Upload apparel pictures directly from local media storage or mobile devices.
* **Price Management**: Dynamic real-time price updates for existing stock.
* **Catalog Control**: Update product names, categories, and descriptions, or delete discontinued items.
* **Data Persistence**: Stores product info dynamically in `products.json` so inventory changes persist across sessions.

---

## 📁 Repository Structure

```text
veteran-online-store/
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── products.json         # Auto-generated product database
├── product_images/       # Directory for uploaded product images
└── README.md             # Project documentation
