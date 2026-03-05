"use client";
import { useState } from 'react';

export default function Home() {
  const [topic, setTopic] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const startAgent = async () => {
    setLoading(true);
    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL;
      const res = await fetch(`${apiUrl}/generate?topic=${encodeURIComponent(topic)}`);
      const data = await res.json();
      setOutput(data.output);
    } catch (err) {
      setOutput("Failed to reach the AI agents.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white p-8 font-sans">
      <div className="max-w-2xl mx-auto space-y-8">
        <header className="text-center">
          <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-emerald-400 bg-clip-text text-transparent">
            Agentic AI Writer
          </h1>
          <p className="text-slate-400 mt-2">Powered by Gemini 1.5 Pro & CrewAI</p>
        </header>

        <div className="flex gap-2">
          <input 
            type="text"
            placeholder="Enter a topic..."
            className="flex-1 bg-slate-900 border border-slate-800 p-3 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
          />
          <button 
            onClick={startAgent}
            disabled={loading || !topic}
            className="bg-blue-600 hover:bg-blue-500 px-6 py-3 rounded-lg font-semibold disabled:opacity-50 transition-all"
          >
            {loading ? "Agents Thinking..." : "Generate Post"}
          </button>
        </div>

        {output && (
          <div className="bg-slate-900 border border-slate-800 p-6 rounded-xl shadow-2xl">
            <h2 className="text-emerald-400 font-bold mb-4 uppercase text-sm tracking-widest">Final Agent Output</h2>
            <div className="prose prose-invert max-w-none whitespace-pre-wrap leading-relaxed">
              {output}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}