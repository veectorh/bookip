/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./*.html",
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,html}",
  ],
  theme: {
    extend: {
      colors: {
        navy: {
          DEFAULT: '#0F1340',
          hover: '#191E51',
          fg: '#B9BEDC',
          mute: '#6F76A8',
        },
        indigo: {
          DEFAULT: '#4353E0',
          hover: '#3948C7', // inferred from original css
          bg: '#EDEFFC',
          subtle: '#EEF0FC',
          line: '#DCE0FA',
          ink: '#2F3CB8',
        },
        ink: '#161A2E',
        muted: '#5F6478',
        canvas: '#F3F4F8',
        surface: '#FFFFFF',
        line: {
          DEFAULT: '#E4E6EE',
          strong: '#CBCFDC',
        },
        th: '#F8F9FC',
        status: {
          draft: { bg: '#F1F2F6', border: '#E4E6EE', dot: '#8B90A6', text: '#454A5E' },
          partiallyPaid: { bg: '#FFF6E5', border: '#F6E3B7', dot: '#D98E00', text: '#8A5A00' },
          paid: { bg: '#E9F7EF', border: '#C8EAD6', dot: '#1E9A5A', text: '#146A3E' },
          overdue: { bg: '#FDECEA', border: '#F5CFC9', dot: '#D0432F', text: '#9A2A1F' },
          sent: { bg: '#EEF0FC', border: '#DCE0FA', dot: '#4353E0', text: '#2F3CB8' },
          cancelled: { bg: '#F5F5F7', border: '#E5E5EA', dot: '#8E8E93', text: '#636366' },
          pending: { bg: '#FFF8E6', border: '#FDE6B0', dot: '#E69900', text: '#8A5A00' },
        },
        imp: {
          bg: '#FFF3D6',
          text: '#5C4300',
          border: '#F0DFAF'
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      fontSize: {
        'xs': '11px',
        'sm': '12px',
        'base': '13px',
        'md': '14px',
        'lg': '15px',
        'xl': '18px',
      },
      borderRadius: {
        DEFAULT: '4px',
        'lg': '8px',
        'xl': '12px',
        'pill': '9999px',
      },
      spacing: {
        'base': '4px',
        'control': '32px',
        'row-desk': '40px',
        'row-mob': '56px',
        'sidebar': '220px',
        'sidebar-collapsed': '56px',
      }
    },
  },
  plugins: [],
}
