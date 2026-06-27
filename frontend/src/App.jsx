import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [leads, setLeads] = useState([]);

  const [form, setForm] = useState({
    name: "",
    phone: "",
    interest: "",
  });

  const [dashboard, setDashboard] = useState({});

  const fetchLeads = async () => {
    const res = await axios.get("http://localhost:8000/leads");
    setLeads(res.data);
  };

  const fetchDashboard = async () => {
    const res = await axios.get(
      "http://localhost:8000/dashboard"
    );

    setDashboard(res.data);
};

  useEffect(() => {
    fetchLeads();
    fetchDashboard();
  }, []);

  const addLead = async () => {
    await axios.post("http://localhost:8000/leads", form);

    fetchLeads();

    setForm({
      name: "",
      phone: "",
      interest: "",
    });
  };

  const updateStatus = async (id, status) => {
    await axios.put(
      `http://localhost:8000/leads/${id}?status=${status}`
    );

    fetchLeads();
  };

  const deleteLead = async (id) => {
    await axios.delete(
      `http://localhost:8000/leads/${id}`
    );

    fetchLeads();
  };

  const searchLead = async (keyword) => {
    if (!keyword) {
      fetchLeads();
      return;
    }

    const res = await axios.get(
      `http://localhost:8000/search?keyword=${keyword}`
    );

    setLeads(res.data);
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>Sales AI CRM</h1>

      <input
        placeholder="Name"
        value={form.name}
        onChange={(e) =>
          setForm({ ...form, name: e.target.value })
        }
      />

      <input
        placeholder="Phone"
        value={form.phone}
        onChange={(e) =>
          setForm({ ...form, phone: e.target.value })
        }
      />

      <input
        placeholder="Interest"
        value={form.interest}
        onChange={(e) =>
          setForm({ ...form, interest: e.target.value })
        }
      />

      <button onClick={addLead}>
        Add Lead
      </button>

      <hr />

      <input
        placeholder="Search Lead"
        onChange={(e) =>
          searchLead(e.target.value)
        }
      />
      <h2>Dashboard</h2>

        <div style={{
          display: "flex",
          gap: "20px",
          flexWrap: "wrap",
          marginBottom: "20px"
        }}>

          <div>Total Leads<br/><b>{dashboard.total}</b></div>

          <div>🔥 HOT<br/><b>{dashboard.hot}</b></div>

          <div>🟡 WARM<br/><b>{dashboard.warm}</b></div>

          <div>🔵 COLD<br/><b>{dashboard.cold}</b></div>

          <div>✅ Qualified<br/><b>{dashboard.qualified}</b></div>

          <div>📞 Contacted<br/><b>{dashboard.contacted}</b></div>

        </div>
      <h2>Leads</h2>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Phone</th>
            <th>Interest</th>
            <th>Score</th>
            <th>Category</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          {leads.map((lead) => (
            <tr key={lead.id}>
              <td>{lead.id}</td>
              <td>{lead.name}</td>
              <td>{lead.phone}</td>
              <td>{lead.interest}</td>
              <td>{lead.score}</td>

              <td>
                {lead.category === "HOT"
                  ? "🔥 HOT"
                  : lead.category === "WARM"
                  ? "🟡 WARM"
                  : "🔵 COLD"}
              </td>

              <td>
                <select
                  value={lead.status}
                  onChange={(e) =>
                    updateStatus(
                      lead.id,
                      e.target.value
                    )
                  }
                >
                  <option>NEW</option>
                  <option>CONTACTED</option>
                  <option>QUALIFIED</option>
                  <option>INTERESTED</option>
                  <option>CLOSED</option>
                  <option>LOST</option>
                </select>
              </td>

              <td>
                <button
                  onClick={() =>
                    deleteLead(lead.id)
                  }
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;