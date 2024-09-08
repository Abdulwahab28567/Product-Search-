{
    'name': 'Find Products in Pos and Stock using Barcode',
    'version': '15.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Find Products in Pos and Stock using Barcode,',
    'description': 'Find Products in Pos and Stock using Barcode',
    'author': 'Abdelwahab',
    'depends': ['point_of_sale', 'stock'],
    'data': [
        'views/stock_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'product_search/static/src/css/pos.css',
            'product_search/static/src/js/find_product_button.js',
            'product_search/static/src/js/find_product.js',
            'product_search/static/src/js/product_details.js',
        ],
        'web.assets_qweb': [
            '/product_search/static/src/xml/find_product_button_templates.xml',
            '/product_search/static/src/xml/find_product_screen_templates.xml',
            '/product_search/static/src/xml/product_details_templates.xml',
            '/product_search/static/src/xml/chrome_templates.xml',
            '/product_search/static/src/xml/dashboard_templates.xml',
        ],
        'web.assets_backend': [
            '/product_search/static/src/css/barcode.css',
            '/product_search/static/src/js/dashboard.js',
        ],
    },

    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
