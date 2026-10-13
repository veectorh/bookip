import { defineConfig } from 'vite';
import handlebars from 'vite-plugin-handlebars';
import { resolve } from 'path';

import fs from 'fs';

const seed = JSON.parse(fs.readFileSync(resolve(__dirname, 'src/data/seed.json'), 'utf-8'));

export default defineConfig({
  server: {
    port: 3000,
  },
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        customers: resolve(__dirname, 'customers.html'),
        quotations: resolve(__dirname, 'quotations.html'),
        purchases: resolve(__dirname, 'purchases.html'),
        vendors: resolve(__dirname, 'vendors.html'),
        employees: resolve(__dirname, 'employees.html'),
        attendance: resolve(__dirname, 'attendance.html'),
        payroll: resolve(__dirname, 'payroll.html'),
        recurring_invoices: resolve(__dirname, 'recurring_invoices.html'),
        components: resolve(__dirname, 'components.html'),
        dashboard: resolve(__dirname, 'dashboard.html'),
        products: resolve(__dirname, 'products.html'),
        product_units: resolve(__dirname, 'product_units.html'),
        accounts: resolve(__dirname, 'accounts.html'),
        transactions: resolve(__dirname, 'transactions.html'),
        departments: resolve(__dirname, 'departments.html'),
        salary_scales: resolve(__dirname, 'salary_scales.html'),
        login: resolve(__dirname, 'login.html'),
        onboarding: resolve(__dirname, 'onboarding.html'),
        settings: resolve(__dirname, 'settings.html'),
        reports_profit_loss: resolve(__dirname, 'reports_profit_loss.html'),
        reports_account_balances: resolve(__dirname, 'reports_account_balances.html'),
        reports_customer_income: resolve(__dirname, 'reports_customer_income.html'),
        reports_vendor_purchases: resolve(__dirname, 'reports_vendor_purchases.html'),
        reports_tax: resolve(__dirname, 'reports_tax.html'),
        admin_dashboard: resolve(__dirname, 'admin_dashboard.html'),
      },
    },
  },
  plugins: [
    handlebars({
      partialDirectory: resolve(__dirname, 'src/partials'),
      context: {
        seed,
      },
      helpers: {
        eq: (a, b) => a === b,
        ne: (a, b) => a !== b,
        or: (...args) => args.slice(0, -1).some(Boolean),
      },
    }),
  ],
});
