# Inventory Management System

A Django-based Inventory Management System for efficiently managing products, suppliers, stock levels, and sales orders. The system supports CRUD operations, stock management, and sales tracking.

## Features

- **Product Management**:
  - Add, list, and manage products with details like name, description, category, price, and stock quantity.
  
- **Supplier Management**:
  - Add, list, and manage suppliers with details like name, email, phone, and address.
  
- **Stock Management**:
  - Record incoming and outgoing stock movements.
  - Validate stock levels and update accordingly.
  
- **Sales Orders**:
  - Create, cancel, and complete sales orders.
  - Automatically update stock levels based on orders.
  
- **Stock Level Checks**:
  - Monitor current stock levels for all products.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB

## Database Models

### Product
- `name` (string)
- `description` (text)
- `category` (string)
- `price` (decimal)
- `stock_quantity` (integer)
- `supplier` (foreign key to Supplier)

### Supplier
- `name` (string)
- `email` (email)
- `phone` (string, 10 digits)
- `address` (text)

### Sale Order
- `product` (foreign key to Product)
- `quantity` (integer)
- `total_price` (decimal)
- `sale_date` (date)
- `status` (Pending/Completed/Cancelled)

### Stock Movement
- `product` (foreign key to Product)
- `quantity` (integer)
- `movement_type` (Incoming/Outgoing)
- `movement_date` (date)
- `notes` (text)

## Setup Instructions

### Prerequisites
- Python 3.8+
- MongoDB
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/inventory-management-system.git
   cd inventory-management-system
