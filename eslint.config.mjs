import nextCoreWebVitals from "eslint-config-next/core-web-vitals";

const eslintConfig = [
  ...nextCoreWebVitals,
  {
    ignores: [".next/**", "out/**", "node_modules/**", "next-env.d.ts", "diabetic-optiscan/**", "dynamic-screen-companion/**"],
  },
];

export default eslintConfig;
