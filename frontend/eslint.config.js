import js from "@eslint/js";
import react from "eslint-plugin-react";

export default [
  js.configs.recommended,
  {
    files: ["src/**/*.{ts,tsx}"],
    plugins: {
        react
    },
    rules: {
        "no-unused-vars": "warn",
        "no-console": "off"
    }
  }
];