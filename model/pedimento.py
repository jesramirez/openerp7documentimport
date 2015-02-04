import openerp
from openerp import netsvc, tools, pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _

class pedimentos(osv.Model):
    _name = 'pedimento.pedimentos.airibuz'
    _columns = {
        'product_id':fields.many2one('product.product', 'Product', requiredñ=True, domain=['|', ('type','=','consu'), ('type','=','product'),'&',('type','=','product'),], help="Product to be counted on this Import")
        'document_import': fields.char('Document Import', size=21, help="Number of document import"),
        'date_border': fiel.date('Start Date'),
        'date_last_mov': fields.date('Date of last movement'),
        'number_border': fields.integer('Number Border, 'help="Number customs import"),
        'city':fields.char('City', size=60, help="City Name Border"),
        'border':fields.char('Border', size=60, help="Number Border"),
        'gln':fields.char('GLN', size=13, help="Number GLN Border"),
        'quantity': fields.float('Quantity',(16,4) help="Quantity of this product on this document")
        }

    _defaults = {

    }

class product_product(osv.Model):
    
    _inherit = 'product.product'
    _columns = {
        'import_document_id': fields.one2many('pedimento.pedimentos.airibuz','product_id', 'Product Accounts'),
        'is_import':fields.boolean('Is import')

    }

    