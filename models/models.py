# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Ajouter un champ texte nommé « exercise » sur l’objet sale.order

class saleorder(models.Model):
    _inherit = "sale.order"
    exercise = fields.Text(string ="exercise")
    to_validate = fields.Boolean("Prêt à valider", default=False)
    customer_discount = fields.Float(string="Remise (%)",  required=False)
    delivery_time = fields.Float(string="Delai de Livraison",  required=False)