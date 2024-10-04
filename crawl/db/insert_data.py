import json
from ..db.database import connect_to_db


def insert_product(product):
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO products (
                tiki_id, sku, name, url_key, url_path, type, author_name, book_cover, brand_name, short_description, price, list_price, badges,
                badges_new, discount, discount_rate, rating_average, review_count, order_count, favourite_count, thumbnail_url, thumbnail_width,
                thumbnail_height, freegift_items, has_ebook, inventory_status, is_visible, productset_id, productset_group_name, seller, is_flower,
                is_gift_card, inventory, url_attendant_input_form, option_color, stock_item, salable_type, seller_product_id, installment_info, url_review,
                bundle_deal, quantity_sold, tiki_live, original_price, shippable, impression_info, advertisement, availability, primary_category_path,
                product_reco_score, seller_id, visible_impression_info, badges_v3
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
            product.get('id', None),  # tiki_id
            product.get('sku', None),
            product.get('name', None),
            product.get('url_key', None),
            product.get('url_path', None),
            product.get('type', None),
            product.get('author_name', None),
            product.get('book_cover', None),
            product.get('brand_name', None),
            product.get('short_description', None),
            product.get('price', None),
            product.get('list_price', None),
            json.dumps(product.get('badges', [])),
            json.dumps(product.get('badges_new', [])),
            product.get('discount', None),
            product.get('discount_rate', None),
            product.get('rating_average', None),
            product.get('review_count', None),
            product.get('order_count', None),
            product.get('favourite_count', None),
            product.get('thumbnail_url', None),
            product.get('thumbnail_width', None),
            product.get('thumbnail_height', None),
            json.dumps(product.get('freegift_items', [])),
            product.get('has_ebook', None),
            product.get('inventory_status', None),
            product.get('is_visible', None),
            product.get('productset_id', None),
            product.get('productset_group_name', None),
            product.get('seller', None),
            product.get('is_flower', None),
            product.get('is_gift_card', None),
            json.dumps(product.get('inventory', None)),
            product.get('url_attendant_input_form', None),
            json.dumps(product.get('option_color', [])),
            json.dumps(product.get('stock_item', None)),
            product.get('salable_type', None),
            product.get('seller_product_id', None),
            json.dumps(product.get('installment_info', None)),
            product.get('url_review', None),
            product.get('bundle_deal', None),
            json.dumps(product.get('quantity_sold', None)),
            product.get('tiki_live', None),
            product.get('original_price', None),
            product.get('shippable', None),
            json.dumps(product.get('impression_info', [])),
            product.get('advertisement', None),
            product.get('availability', None),
            product.get('primary_category_path', None),
            product.get('product_reco_score', None),
            product.get('seller_id', None),
            json.dumps(product.get('visible_impression_info', {})),
            json.dumps(product.get('badges_v3', []))
        ))
