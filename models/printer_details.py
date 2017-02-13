# -*- coding: utf-8 -*-

from openerp import models, fields, api
import string
import random
from openerp.http import request
from datetime import datetime,timedelta,date

SELECTIONS = [
    ('m1', 'Modello1'),
    ('m2', 'Modello2'),
    ('m3', 'Modello3'),
    ('m4', 'Modello4'),
    ('m5', 'Modello5'),
]

class printer_details(models.Model):
    _name = 'odoo_printers.printer_details'

    
    model = fields.Selection(SELECTIONS,string="Modello",required=True)
    serial = fields.Char(string="Seriale",required=True)
    
    #TODO linka il cliente vero di odoo o no?
    client = fields.Char(string="Cliente",required=True)
    
    tot_bw = fields.Integer(string="Totale stampe in bianco e nero", default=0)
    tot_col = fields.Integer(string="Totale stampe a colori", default=0)
    toner_black = fields.Integer(string="Livello toner nero", default=100)
    toner_red = fields.Integer(string="Livello toner rosso", default=100)
    toner_blue = fields.Integer(string="Livello toner blu", default=100)
    toner_yellow = fields.Integer(string="Livello toner giallo", default=100)
    months = fields.Many2many('odoo_printers.monthly_meters')
    

    @api.model
    def create(self, vals):
        model = vals['model']
        serial = vals['serial']
        client = vals['client']
        tot_bw = vals['tot_bw']
        tot_col = vals['tot_col']
        toner_black = vals['toner_black']
        toner_red = vals['toner_red']
        toner_blue = vals['toner_blue']
        toner_yellow = vals['toner_yellow']
        
        res = super(printer_details, self).create(vals)
        return res
    

    
class monthly_meters(models.Model):
    _name = 'odoo_printers.monthly_meters'
    
   
    month = fields.Char(string="stringa mese-anno")
    bw = fields.Integer(string="numero totale stampe in bianco e nero mensili", default=0)
    col = fields.Integer(string="numero totale stampe a colori mensili", default=0)
    #printer = fields.Many2one('odoo_printers.printer_details')
    
