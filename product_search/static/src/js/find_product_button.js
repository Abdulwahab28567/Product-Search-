/** @odoo-module **/
odoo.define('product_detail_search.find_product_button_custom', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const { useListener } = require("@web/core/utils/hooks");
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');

    class FindProductButton extends PosComponent {
        setup() {
            super.setup();
            useListener('click', this.onClick);
        }

        async onClick() {
            this.showScreen('FindProductScreen');
            this.trigger('search-product');
        }
    }

    FindProductButton.template = 'FindProductButton';

    ProductScreen.addControlButton({
        component: FindProductButton,
        condition: function() {
            return true;
        },
        position: 'after',
    });

    Registries.Component.add(FindProductButton);

    return FindProductButton;
});
