##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    manufacturer_pref = fields.Char('Manufacturer Product Code')

    @api.model
    def create(self, vals):
        template_id = vals.get("product_tmpl_id")
        if template_id:
            if "manufacturer_pref" not in vals:
                pref = self.env["product.template"].browse(
                    template_id).manufacturer_pref
                vals.update({"manufacturer_pref": pref})
        return super(ProductProduct, self).create(vals)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    manufacturer = fields.Many2one('res.partner', 'Manufacturer')
    manufacturer_pname = fields.Char('Manufacturer Product Name')
    manufacturer_pref = fields.Char('Manufacturer Product Code')
