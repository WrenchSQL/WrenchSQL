from gi.repository import Gtk

import datetime
from pprint import pprint
class mysql(object):
    # Numeric
    BIT = bytes
    # Integer
    INTEGER = int
    INT = INTEGER
    SMALLINT = int
    TINYINT = int
    MEDIUMINT = int
    BIGINT = int
    # FixedPoint
    DECIMAL = float
    DOUBLE = float
    # FloatingPoint
    FLOAT = float
    DOUBLE = float

    # Datetime
    DATE = datetime.date
    TIEMSTAMT = datetime.date.fromtimestamp
    YEAR = datetime.date

    # String
    CHAR = str
    VARCHAR = str
    BINARY = bytes
    BLOB = str
    TEXT = str
    ENUM = str
    SET = str

show_create_table = """
CREATE TABLE `dealer_ava_leads` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `bs_id` int(11) DEFAULT NULL,
  `requestdate` datetime DEFAULT NULL,
  `insert_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `lead_type` varchar(50) NOT NULL DEFAULT 'unknown',
  `status` enum('active','inactive','manual_deactivate','invalid email','dupe','undeliverable','excluded') CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL DEFAULT 'active',
  `last_modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `subject` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `lead_to_address` varchar(150) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `lead_from_address` varchar(150) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `lead_reply_to` varchar(150) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `message_key` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `vehicle_status` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `vehicle_interest` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `source` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `source_id` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `year` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `make` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `model` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `vin` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `stock` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `trim` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `bodystyle` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `transmission` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `odometer` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `interiorcolor` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `exteriorcolor` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `preference` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `price` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `currency` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `pricecomments` varchar(450) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `option` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_first_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_last_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_email` varchar(500) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_phone` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_phone_work` varchar(25) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `customer_phone_cell` varchar(25) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `customer_phone_time` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_address` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_city` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_state` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_zip` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_country` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_timeframe` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `customer_comments` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `provider_name` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `dealer_id` int(11) NOT NULL,
  `rep_id` int(11) NOT NULL DEFAULT '0',
  `campaign_id` int(11) NOT NULL DEFAULT '0',
  `email_id` int(11) DEFAULT NULL,
  `original_message` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `type` varchar(18) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `prospect_create_time` datetime DEFAULT NULL,
  `to_address` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `from_address` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `inbox_date` datetime DEFAULT NULL,
  `customer_phone_from_msg` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `contact1_first_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `contact1_last_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `contact1_cell_phone` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `contact1_cell_provider` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `contact1_email_address` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `dupe_email_address` tinyint(3) unsigned DEFAULT '0',
  `bs_ava_alias` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT 'Jenny',
  `reactivation_date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`) KEY_BLOCK_SIZE=16,
  KEY `requestdate_idx` (`requestdate`) KEY_BLOCK_SIZE=16,
  KEY `source_id` (`source_id`) KEY_BLOCK_SIZE=16,
  KEY `dealer_requestdate` (`dealer_id`,`requestdate`) KEY_BLOCK_SIZE=16,
  KEY `dealer_status` (`dealer_id`,`status`) KEY_BLOCK_SIZE=16,
  KEY `last_modified` (`last_modified`) KEY_BLOCK_SIZE=16,
  KEY `campaignid_dealerid` (`campaign_id`,`dealer_id`) KEY_BLOCK_SIZE=16,
  KEY `rep_id` (`rep_id`) KEY_BLOCK_SIZE=16,
  KEY `dlr_src_rep` (`dealer_id`,`source_id`,`rep_id`) KEY_BLOCK_SIZE=16,
  KEY `dlr_src4` (`dealer_id`,`source_id`(4)) KEY_BLOCK_SIZE=16,
  KEY `dlr_lead2_src2` (`dealer_id`,`lead_type`(2),`source_id`(2)) KEY_BLOCK_SIZE=16,
  KEY `customer_email16` (`customer_email`(16)) KEY_BLOCK_SIZE=16,
  KEY `dlr_src_rep_dupe` (`dealer_id`,`source_id`,`rep_id`,`dupe_email_address`) KEY_BLOCK_SIZE=16,
  KEY `insert_date` (`insert_date`) KEY_BLOCK_SIZE=16,
  KEY `lead_type` (`lead_type`) KEY_BLOCK_SIZE=16,
  KEY `dlr_status_leadtype` (`dealer_id`,`status`,`lead_type`) KEY_BLOCK_SIZE=16,
  KEY `dlr_insert_date` (`dealer_id`,`insert_date`)
) ENGINE=InnoDB AUTO_INCREMENT=11300443 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8
"""

import sqlparse
# help(sqlparse.tokens)
statement = sqlparse.parse(show_create_table)[0]
for x in statement.tokens[
    statement.token_index(
        statement.token_next_by_type(0, sqlparse.tokens.DDL)
    ) + 4
].flatten():
    if x.match(sqlparse.tokens.Name, '.*', True):
        print(x)
# pprint(
#     [0].match()
# )
# class CellRendererTextWindow(Gtk.Window):

#     def __init__(self):
#         Gtk.Window.__init__(self, title="CellRendererText Example")

#         self.set_default_size(200, 200)



#         # create a new scrolled window.
#         scrolled_window = Gtk.ScrolledWindow()
#         scrolled_window.set_border_width(10)

#         # the policy is one of POLICY AUTOMATIC, or POLICY_ALWAYS.
#         # POLICY_AUTOMATIC will automatically decide whether you need
#         # scrollbars, whereas POLICY_ALWAYS will always leave the scrollbars
#         # there. The first one is the horizontal scrollbar, the second, the
#         # vertical.
#         scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.ALWAYS)

#         # The dialog window is created with a vbox packed into it.
#         scrolled_window.show()
#         self.add(scrolled_window)
#         self.scrolled_window = scrolled_window


#         self.liststore = Gtk.ListStore(str, str)
#         self.liststore.append(["Fedora", "http://fedoraproject.org/"])
#         self.liststore.append(["Slackware", "http://www.slackware.com/"])
#         self.liststore.append(["Sidux", "http://sidux.com/"])
#         self.liststore.append(["Sidux", "http://sidux.com/"])
#         self.liststore.append(["Sidux", "http://sidux.com/"])
#         self.liststore.append(["Sidux", "http://sidux.com/"])
#         self.liststore.append(["Sidux", "http://sidux.com/"])
#         self.liststore.append(["Sidux", "http://sidux.com/"])
#         self.liststore.append(["Sidux", "http://sidux.com/"])
#         self.liststore.append(["Sidux", "http://sidux.com/"])

#         treeview = Gtk.TreeView(model=self.liststore)

#         renderer_text = Gtk.CellRendererText()
#         column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
#         treeview.append_column(column_text)

#         renderer_editabletext = Gtk.CellRendererText()
#         renderer_editabletext.set_property("editable", True)

#         column_editabletext = Gtk.TreeViewColumn("Editable Text",
#             renderer_editabletext, text=1)
#         treeview.append_column(column_editabletext)

#         renderer_editabletext.connect("edited", self.text_edited)

#         self.scrolled_window.add(treeview)

#     def text_edited(self, widget, path, text):
#         self.liststore[path][1] = text

# win = CellRendererTextWindow()
# win.connect("delete-event", Gtk.main_quit)
# win.show_all()
# Gtk.main()
