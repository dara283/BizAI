<template>
  <div class="content">

    <section class="input-section">
      <div class="section-header">
        <label class="section-label">Business Data Input</label>
        <span class="char-count">{{ input.length }} characters</span>
      </div>
      <textarea
        v-model="input"
        placeholder="Paste your business report, financial data, sales figures, or any business text here..."
        :disabled="loading"
      ></textarea>
      <div class="input-actions">
        <button class="btn-clear" @click="clear" :disabled="!input && !result">Clear</button>
        <button class="btn-analyse" @click="analyse" :disabled="loading || !input.trim()">
          <span v-if="loading" class="spinner"></span>
          {{ loading ? "Analysing..." : "Run Analysis" }}
        </button>
      </div>
    </section>

    <div v-if="error" class="error-banner">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
      {{ error }}
    </div>

    <transition name="fade">
      <section v-if="result" class="results-section">
        <div class="results-grid">

          <div class="result-card">
            <div class="result-card-header">
              <div class="result-icon summary-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/>
                  <line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>
                </svg>
              </div>
              <span>Summary</span>
            </div>
            <p>{{ result.summary }}</p>
          </div>

          <div class="result-card">
            <div class="result-card-header">
              <div class="result-icon insights-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
                </svg>
              </div>
              <span>Key Insights</span>
            </div>
            <p>{{ result.insights }}</p>
          </div>

          <div class="result-card full-width">
            <div class="result-card-header">
              <div class="result-icon reco-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                  <polyline points="22 4 12 14.01 9 11.01"/>
                </svg>
              </div>
              <span>Recommendations</span>
            </div>
            <p>{{ result.recommendations }}</p>
          </div>

        </div>
      </section>
    </transition>

  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      input: "",
      result: null,
      loading: false,
      error: null
    };
  },
  methods: {
    async analyse() {
      this.loading = true;
      this.error = null;
      this.result = null;
      try {
        const res = await axios.post("http://127.0.0.1:5000/analyse", { text: this.input });
        this.result = res.data;
        const history = JSON.parse(localStorage.getItem("analysisHistory") || "[]");
        history.unshift({
          id: Date.now(),
          date: new Date().toLocaleString(),
          preview: this.input.slice(0, 80) + (this.input.length > 80 ? "..." : ""),
          result: this.result
        });
        localStorage.setItem("analysisHistory", JSON.stringify(history.slice(0, 50)));
      } catch (err) {
        this.error = "Unable to connect to the analysis server. Please ensure the backend is running on port 5000.";
      } finally {
        this.loading = false;
      }
    },
    clear() {
      this.input = "";
      this.result = null;
      this.error = null;
    }
  }
};
</script>
