# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import methods

class backend_felix1gruppen(models.Model):
    _name='backend.felix1gruppen'
    _inherit='backend.methods.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char(String="Gruppe")
    description=fields.Text('Beschreibung')