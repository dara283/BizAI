<template>
  <div class="content">

    <div class="page-header">
      <div>
        <h2 class="view-title">Settings</h2>
        <p class="view-subtitle">Configure your backend connection and analysis preferences.</p>
      </div>
    </div>

    <div class="settings-grid">

      <div class="settings-card">
        <h3 class="settings-section-title">Backend Connection</h3>

        <div class="field">
          <label>API Base URL</label>
          <input v-model="settings.apiUrl" type="text" placeholder="http://127.0.0.1:5000" />
          <span class="field-hint">The URL where your Flask backend is running.</span>
        </div>

        <div class="field">
          <label>Connection Status</label>
          <div class="connection-row">
            <div class="status-pill" :class="pingStatus">
              <span class="dot"></span>
              {{ pingLabel }}
            </div>
            <button class="btn-secondary" @click="ping" :disabled="pinging">
              {{ pinging ? "Checking..." : "Test Connection" }}
            </button>
          </div>
        </div>
      </div>

      <div class="settings-card">
        <h3 class="settings-section-title">Analysis Preferences</h3>

        <div class="field">
          <label>AI Model</label>
          <select v-model="settings.model">
            <option value="gpt-3.5-turbo">GPT-3.5 Turbo — Faster, lower cost</option>
            <option value="gpt-4">GPT-4 — More accurate, higher cost</option>
            <option value="gpt-4o">GPT-4o — Recommended</option>
          </select>
          <span class="field-hint">Model selection requires backend support.</span>
        </div>

        <div class="field">
          <label>Response Language</label>
          <select v-model="settings.language">
            <option value="English">English</option>
            <option value="French">French</option>
            <option value="Spanish">Spanish</option>
            <option value="German">German</option>
            <option value="Portuguese">Portuguese</option>
          </select>
        </div>
      </div>

      <div class="settings-card">
        <h3 class="settings-section-title">Data & Privacy</h3>
        <div class="field">
          <label>Analysis History</label>
          <p class="field-hint" style="margin-bottom: 12px;">All history is stored locally in your browser. Nothing is sent to external servers beyond the OpenAI API call.</p>
          <button class="btn-danger" @click="clearHistory">Clear All History</button>
        </div>
      </div>

    </div>

    <div class="settings-footer">
      <button class="btn-analyse" @click="save">Save Settings</button>
      <span v-if="saved" class="saved-label">Settings saved.</span>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      settings: {
        apiUrl: "http://127.0.0.1:5000",
        model: "gpt-3.5-turbo",
        language: "English"
      },
      pingStatus: "idle",
      pingLabel: "Not tested",
      pinging: false,
      saved: false
    };
  },
  mounted() {
    const stored = localStorage.getItem("bizaiSettings");
    if (stored) this.settings = { ...this.settings, ...JSON.parse(stored) };
  },
  methods: {
    save() {
      localStorage.setItem("bizaiSettings", JSON.stringify(this.settings));
      this.saved = true;
      setTimeout(() => (this.saved = false), 2500);
    },
    async ping() {
      this.pinging = true;
      this.pingStatus = "idle";
      this.pingLabel = "Checking...";
      try {
        await fetch(this.settings.apiUrl + "/analyse", { method: "OPTIONS" });
        this.pingStatus = "ok";
        this.pingLabel = "Connected";
      } catch {
        this.pingStatus = "fail";
        this.pingLabel = "Unreachable";
      } finally {
        this.pinging = false;
      }
    },
    clearHistory() {
      localStorage.removeItem("analysisHistory");
      alert("History cleared.");
    }
  }
};
</script>
