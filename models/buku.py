from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    title = fields.Char(string='Judul', required=True)
    category = fields.Selection([('umum', 'Umum'),('it', 'IT'),('kesehatan', 'Kesehatan'),('politik', 'Politik')], string='Category', required=True)
    publish_date = fields.Date(string='Tanggal Terbit')
    author_ids = fields.Many2many('res.partner', string='Penulis')
    isbn_code = fields.Char(string='Kode ISBN', required=True, unique=True)

    name = fields.Char(string='Book Title', required=True)
    serial_number = fields.Char(string='Serial Number', required=True, copy=False)
    location = fields.Char(string='Lokasi')
    qty_available = fields.Integer(string='Qty Tersedia', default=1)
