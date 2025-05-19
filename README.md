# 🩺 Unfriend-Diabetes

**Unfriend-Diabetes** is a comprehensive, AI-powered health application designed to assist individuals in managing and understanding their diabetes more effectively. With advanced features like voice and text input, image analysis, health tracking, and AI-generated insights, this app empowers users to take control of their health data in a secure and user-friendly environment.

---

## 🌟 Key Features

### 🎙️ Voice & Text Input
- Interact using natural voice commands or text queries.
- Powered by NLP (Natural Language Processing) for accurate understanding.
- Supports multiple languages for accessibility.
- Ideal for users who prefer hands-free operation or have vision impairments.

### 🖼️ Image Analysis
- Upload images related to diabetes such as:
  - Food items for carb estimation.
  - Wounds for healing status analysis.
  - Glucose monitor screen readings.
- AI provides visual analysis, predictions, and recommendations.
- Stores image history to track changes over time.

### 📊 Health Data Tracking
- Track and visualize key health metrics:
  - Blood glucose levels.
  - Blood pressure readings.
  - Heart rate data.
- Interactive charts to help understand trends and patterns.
- Manual and automated data entry options.

### 💊 Medication Management
- Log and monitor current medications and dosages.
- Set up daily/weekly reminders to prevent missed doses.
- Access medication history and adherence analytics.
- AI provides drug interaction warnings and recommendations.

### 📄 Medical Report Generation
- Automatically generate professional PDF health reports.
- Reports include vital signs, medication logs, image analyses, and trends.
- Share reports with healthcare providers for more informed consultations.

### 🧠 AI-Powered Insights
- Get smart, personalized insights from your data:
  - Dietary recommendations.
  - Glucose level trends and risk alerts.
  - Medication impact analysis.
- Learn how lifestyle choices affect diabetes management.

### 🔒 Security & Privacy
- Secure login system with encrypted user data.
- Environment-based protection of sensitive credentials (API keys, DB access).
- Compliant with privacy best practices.
- Regular security updates to ensure data safety.

---

## 🚀 Getting Started

### 📋 Prerequisites

Make sure the following are installed:
- Python 3.10 or higher
- [MongoDB](https://www.mongodb.com/) (for data storage)

---

### 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Deekshithadasari26/Unfriend-Diabetes.git
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and add:
   ```env
   MONGODB_URI=your_mongodb_uri
   GOOGLE_API_KEY=your_google_api_key
   ```

5. **Run the application:**
   ```bash
   streamlit run diabetes_assistant.py
   ```

---

## 🧪 Technologies Used

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend:** Python, MongoDB
- **AI/ML Libraries:** OpenAI API, Pillow, TensorFlow (optional for image models)
- **Speech Recognition:** Google Speech API, FFmpeg
- **PDF Reports:** ReportLab, FPDF
- **Security:** Dotenv, Token-based auth

---

## 🤝 Contributing

We welcome contributions of all kinds—bug fixes, improvements, and new features.

To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes.
4. Commit and push: `git commit -m "Add new feature" && git push`
5. Open a pull request on GitHub.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

For questions, feedback, or contributions, please open an [issue](https://github.com/Deekshithadasari26/Unfriend-Diabetes/issues) or submit a pull request via the [GitHub repository](https://github.com/Deekshithadasari26/Unfriend-Diabetes).
