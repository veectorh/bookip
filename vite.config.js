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
