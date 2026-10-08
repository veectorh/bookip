import { defineConfig } from 'vite';
import handlebars from 'vite-plugin-handlebars';
import { resolve } from 'path';

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
      },
    },
  },
  plugins: [
    handlebars({
      partialDirectory: resolve(__dirname, 'src/partials'),
    }),
  ],
});
