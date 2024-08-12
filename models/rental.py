
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryRental(models.Model):
    _name = 'library.rental'
    _description = 'Library Rental'

    rental_date = fields.Date(string='Tanggal Rental', default=fields.Date.today)
    member_id = fields.Many2one('library.member', string='Nama Peminjam', required=True)
    rental_line_ids = fields.One2many('library.rental.line', 'rental_id', string='List Buku yang Dipinjam')
    state = fields.Selection([
        ('ongoing', 'Sedang Dipinjam'),
        ('returned', 'Belum Dikembalikan'),
        ('done', 'Selesai')
    ], string='Status Transaksi', default='ongoing')


class LibraryRentalLine(models.Model):
    _name = 'library.rental.line'
    _description = 'Library Rental Line'

    rental_id = fields.Many2one('library.rental', string='Rental Reference', required=True)
    book_id = fields.Many2one('library.book', string='Buku', required=True)
    location = fields.Char(related='book_id.location', string='Lokasi')
    stock = fields.Integer(related='book_id.qty_available', string='Stok Buku')
    quantity = fields.Integer(string='Jumlah Buku Dipinjam', required=True)
    start_date = fields.Date(string='Tanggal Mulai', default=fields.Date.today)
    end_date = fields.Date(string='Tanggal Selesai')
    total_cost = fields.Float(string='Total Biaya Sewa', compute='_compute_total_cost')
    is_returned = fields.Boolean(string='Pengembalian', default=False)

    @api.depends('quantity')
    def _compute_total_cost(self):
        for line in self:
            # Misalnya harga sewa per buku 10
            line.total_cost = line.quantity * 10

    @api.model
    def create(self, vals):
        if not vals.get('rental_id'):
            raise ValidationError('Rental Reference must be set.')
        return super(LibraryRentalLine, self).create(vals)
