<template>
  <div class="content">

    <div class="page-header">
      <div>
        <h2 class="view-title">Analysis History</h2>
        <p class="view-subtitle">Your last {{ history.length }} analyses are stored locally on this device.</p>
      </div>
      <button v-if="history.length" class="btn-danger" @click="clearAll">Clear All</button>
    </div>

    <div v-if="!history.length" class="empty-state">
      <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
      </svg>
      <p>No analyses yet. Run your first analysis to see it here.</p>
    </div>

    <div v-else class="history-list">
      <div v-for="item in history" :key="item.id" class="history-card">
        <div class="history-card-top">
          <div class="history-meta">
            <span class="history-date">{{ item.date }}</span>
            <p class="history-preview">{{ item.preview }}</p>
          </div>
          <div class="history-actions">
            <button class="btn-icon" @click="toggle(item.id)" :title="expanded === item.id ? 'Collapse' : 'Expand'">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline v-if="expanded === item.id" points="18 15 12 9 6 15"/>
                <polyline v-else points="6 9 12 15 18 9"/>
              </svg>
            </button>
            <button class="btn-icon danger" @click="remove(item.id)" title="Delete">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14H6L5 6"/><path d="M10 11v6"/><path d="M14 11v6"/><path d="M9 6V4h6v2"/>
              </svg>
            </button>
          </div>
        </div>

        <transition name="fade">
          <div v-if="expanded === item.id" class="history-results">
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
                <p>{{ item.result.summary }}</p>
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
                <p>{{ item.result.insights }}</p>
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
                <p>{{ item.result.recommendations }}</p>
              </div>
            </div>
          </div>
        </transition>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      history: [],
      expanded: null
    };
  },
  mounted() {
    this.history = JSON.parse(localStorage.getItem("analysisHistory") || "[]");
  },
  methods: {
    toggle(id) {
      this.expanded = this.expanded === id ? null : id;
    },
    remove(id) {
      this.history = this.history.filter(h => h.id !== id);
      localStorage.setItem("analysisHistory", JSON.stringify(this.history));
      if (this.expanded === id) this.expanded = null;
    },
    clearAll() {
      this.history = [];
      this.expanded = null;
      localStorage.removeItem("analysisHistory");
    }
  }
};
</script>
