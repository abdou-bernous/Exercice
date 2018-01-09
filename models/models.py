# -*- coding: utf-8 -*-

from odoo import models, fields, api


# Ajouter un champ texte nommé « exercise » sur l’objet sale.order

class sale_order(models.Model):
    _inherit = "sale.order"
    exercise = fields.Text()
    final_customer_id = fields.Many2one(comodel_name="res.partner", string="Client Final", required=False,domain="[('active','=',True)]" )
    to_validate = fields.Boolean("Prêt à valider", default=False, copie=False)
    remise_client = fields.Float(string="Remise (%)",  required=False, readonly= True)
    delai_livraison = fields.Float(string="Delai de Livraison",  required=False,)