# BetterPrompt

**BetterPrompt** is an experimental tool designed to showcase how refining a vague prompt into a structured, goal-driven format can drastically improve the quality of responses produced by large language models (LLMs) such as ChatGPT.

By simulating multi-step reasoning and automatic prompt enhancement, BetterPrompt demonstrates how to unlock richer, more relevant, and more actionable AI outputs — with minimal user effort.

---

## 🔍 Project Overview

Many users struggle to get the most out of LLMs simply because their prompts are too vague. BetterPrompt takes a basic user prompt and applies several steps:

1. **Generates an initial answer using the original input**
2. **Creates a "Perfect Prompt" with detailed structure (goal, format, context, warnings)**
3. **Rewrites the perfect prompt into natural form and improves it further**
4. **Sends the final version to the LLM for an enhanced answer**
5. **Optionally compares both answers**

---

## 📊 Real-World Test: Nutrition Prompt

### 🧾 Original Prompt
"voglio avere un alimentazione bilanciata" Italian Prompt

### ✏️ Initial AI Answer
> Ottima scelta!
>
> Avere un'alimentazione bilanciata è fondamentale per mantenere una buona salute fisica e mentale. Ecco alcuni consigli...
>
> 1. Varietà di alimenti  
> 2. Porzioni adeguate  
> 3. Idratazione  
> 4. Limita i cibi processati  
> 5. Cena equilibrata  
> 6. Non saltare i pasti  
> 7. Pianifica i pasti  
> 8. Consulta un nutrizionista  

✅ **Good general advice** — but vague and generic. Not structured, not actionable.

---

### 🔁 Improved Prompt (Generated Internally)
> Create a personalized dietary plan aimed at achieving a balanced, healthy lifestyle. Include detailed portion sizes, meal planning strategies for 7 days, nutritional guidelines, and practical advice for sustainable eating habits. The response should be in Italian and address hydration, food group balance, and eating behaviors.

---

### 🧠 Final AI Answer
> **Piano Alimentare Personalizzato**
>
> **Introduzione:**  
> Una dieta equilibrata è fondamentale per il benessere generale...
>
> **Piano Consigliato:**  
> - Frutta e verdura: 5 porzioni  
> - Proteine: 2-3 porzioni  
> - Carboidrati complessi: 3-4 porzioni  
> - Grassi sani: 2-3 porzioni  
>
> **Piano Pasti di 7 Giorni:**  
> Lunedì: omelette, pollo con avocado, pesce al forno...  
> Martedì: yogurt con frutta, sandwich, pollo grigliato...
>
> **Consigli Utili:**  
> - Bevi acqua  
> - Mangia lentamente  
> - Evita schermi durante i pasti  
> - Preferisci cibi stagionali  
>
> ✅ Highly structured, specific, practical, and deeply useful.

---

## 🧾 Comparison Summary

| Feature                        | Initial Response | Final Response |
|-------------------------------|------------------|----------------|
| Personalization                | ❌ No            | ✅ Yes         |
| Structure / Formatting         | ⚠️ Basic         | ✅ Rich        |
| Day-by-Day Meal Plan           | ❌ No            | ✅ Yes         |
| Practical Tips                 | ✅ Some          | ✅ Comprehensive |
| Language / Context Awareness   | ✅ Yes           | ✅ Yes         |

**Result:** BetterPrompt enables users to obtain higher-value responses from AI with zero prompt-writing experience.

---

## 🛠️ Installation & Usage (Coming Soon)

The full implementation is written in Python and leverages Groq (via API) and OpenAI tools. A CLI interface and interactive terminal-based prompt debugger are currently in development.

---

## 🧑‍💻 Author

Developed with ❤️ by **Biagio Lernetti**  
GitHub: [@blaze534new](https://github.com/blaze534new)

---

## ⚖️ License

This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

You are free to:

- Share — copy and redistribute the material in any medium or format  
- Adapt — remix, transform, and build upon the material  

**Under the following terms:**

- **Attribution** — You must give appropriate credit to Biagio Lernetti  
- ❌ No requirement to open-source or share modifications  
- ❌ No requirement to distribute under same license  

Read more here: [https://creativecommons.org/licenses/by/4.0](https://creativecommons.org/licenses/by/4.0)

---
