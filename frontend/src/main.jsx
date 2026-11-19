import "@vitejs/plugin-react/preamble";

import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import "./index.css";

const rootElement = document.getElementById("root");

const designId = rootElement.dataset.designId;

createRoot(rootElement).render(
    <App designId={designId} />
);
