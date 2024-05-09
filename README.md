# Odoo v17 

You can integrate Hesabe Payment Gateway in your Odoo v17 by following the steps given below:<br/>

#### Important Notes

Before utilizing this module, ensure you have installed the 'pycryptodome' Python library for encryption purposes. Additionally, make sure your store has the Odoo Payment and eCommerce modules installed. It's important to configure all your accounting settings before using this Odoo module. In some cases, changes made in Odoo may not apply to the system immediately, so after major changes, please restart your Odoo server.
<br/>
#### Installation Steps

1. Download plugin from here : <br/>

   **Odoo v17**  
   [Download Plugin](https://github.com/hesabe-tech-team/api2-plugin-odoo/tree/odoo-v17)

2. After you download plugin you need to extract and copy 'hesabepayment' folder to your odoo installation path\server\odoo\addons directory.

3. Go to Apps → Search hesabepayment module. → Click Install module
   ![Odoo 1](https://hesabe-assets.s3.me-south-1.amazonaws.com/kits/search-page.png)
4. You need to activate Hesabe Payment Provider from website -> configuration -> Payment Providers
5. You need to activate Hesabe Payment Method from website -> configuration -> Payment Methods  
   ![Odoo 3](https://hesabe-assets.s3.me-south-1.amazonaws.com/kits/payment-method.png)
6. Configure the credential information which consists of Merchant Code, Access Code,Working Key, IV Key and API Version. Make sure you use correct credentials for Test and Production.
   ![Odoo 4](https://hesabe-assets.s3.me-south-1.amazonaws.com/kits/payment-provider-setting.png)
