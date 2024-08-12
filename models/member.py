from odoo import models, fields

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'
    
    name = fields.Char(string='Name', required=True)
    no_identitas = fields.Char(string='No Identitas', required=True, unique=True)
    jenis_kartu_identitas = fields.Selection([
        ('ktp', 'KTP'),
        ('sim', 'SIM'),
        ('passport', 'Passport')
    ], string='Jenis Kartu Identitas', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved')
    ], string='State', default='draft')
