import React, { useState, useEffect, useRef } from 'react';
import { Play, Loader2, CheckCircle, XCircle, Clock, ChevronRight, Activity, Terminal } from 'lucide-react';

function App() {
  const [goal, setGoal] = useState('');
  const [taskId, setTaskId] = useState(null);
  const [status, setStatus] = useState('idle'); // idle, pending, running, completed, failed
  const [data, setData] = useState(null);
  const [logs, setLogs] = useState([]);
  
  const intervalRef = useRef(null);
  const logsEndRef = useRef(null);

  // Auto-scroll logs to bottom
  useEffect(() => {
    logsEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [logs]);

  const runTask = async () => {
    if (!goal.trim()) return;
    
    setStatus('pending');
    setLogs([{ type: 'info', msg: 'Starting task...', time: new Date() }]);
    setData(null);
    setTaskId(null);

    if (intervalRef.current) clearInterval(intervalRef.current);

    try {
      const res = await fetch('http://localhost:8000/api/run-task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ goal })
      });
      
      if (!res.ok) throw new Error('API Error');
      const result = await res.json();
      
      setTaskId(result.task_id);
      
      intervalRef.current = setInterval(() => checkStatus(result.task_id), 2000);
    } catch (err) {
      console.error(err);
      setStatus('failed');
      setLogs(prev => [...prev, { type: 'error', msg: 'Failed to start task. Is the server running?', time: new Date() }]);
    }
  };

  const checkStatus = async (id) => {
    try {
      const res = await fetch(`http://localhost:8000/api/status/${id}`);
      if (!res.ok) return;
      const result = await res.json();
      
      setStatus(result.status);
      setData(result.data);
      
      // Compute delta logs
      const steps = result.data?.steps || [];
      const newLogs = steps.map((step, idx) => ({
        id: idx,
        type: 'step',
        msg: `[${step.step.toUpperCase()}] Completed execution.`,
        data: step.data,
        time: new Date()
      }));
      
      if (newLogs.length > 0) {
        setLogs(prev => {
          // just a simple dedup logic for demo:
          const existingIds = new Set(prev.map(l => l.id));
          const uniqueNewLogs = newLogs.filter(l => !existingIds.has(l.id));
          return [...prev, ...uniqueNewLogs];
        });
      }

      if (result.status === 'completed' || result.status === 'failed') {
        clearInterval(intervalRef.current);
        setLogs(prev => [...prev, { 
          type: result.status === 'completed' ? 'success' : 'error', 
          msg: `Task ${result.status}.`, 
          time: new Date() 
        }]);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const getStatusIcon = () => {
    switch(status) {
      case 'idle': return <Clock className="text-surface-400 w-5 h-5" />;
      case 'pending':
      case 'running': return <Loader2 className="text-primary-500 w-5 h-5 animate-spin" />;
      case 'completed': return <CheckCircle className="text-green-500 w-5 h-5" />;
      case 'failed': return <XCircle className="text-red-500 w-5 h-5" />;
      default: return <Clock className="text-surface-400 w-5 h-5" />;
    }
  };

  const renderValue = (val) => {
    if (val === null || val === undefined) return 'N/A';
    if (typeof val !== 'object') return <span className="text-surface-300">{String(val)}</span>;
    
    if (Array.isArray(val)) {
      return (
        <ul className="list-disc pl-5 mt-1 space-y-2 marker:text-surface-500">
          {val.map((item, idx) => (
            <li key={idx}>
              {typeof item === 'object' ? renderValue(item) : <span className="text-surface-300">{String(item)}</span>}
            </li>
          ))}
        </ul>
      );
    }
    
    return (
      <div className="mt-1 pl-3 border-l-2 border-surface-700 space-y-1">
        {Object.entries(val).map(([k, v]) => (
          <div key={k}>
            <span className="text-primary-300 font-semibold capitalize">{k.replace(/_/g, ' ')}:</span> {renderValue(v)}
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-surface-50 text-surface-900 font-sans selection:bg-primary-200">
      {/* Background decoration */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none z-0">
        <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] rounded-full bg-primary-200/40 blur-3xl opacity-50"></div>
        <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] rounded-full bg-indigo-200/40 blur-3xl opacity-50"></div>
      </div>

      <div className="max-w-6xl mx-auto px-4 py-12 relative z-10 flex flex-col gap-8">
        
        {/* Header */}
        <header className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-primary-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-primary-500/30">
              <Activity className="text-white w-5 h-5" />
            </div>
            <div>
              <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-surface-900 to-surface-600">
                AgentFlow Platform
              </h1>
              <p className="text-sm text-surface-500 font-medium">Multi-Agent Orchestration System</p>
            </div>
          </div>
        </header>

        <main className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          {/* Left Column: Input & Info */}
          <div className="lg:col-span-1 flex flex-col gap-6">
            <div className="bg-white/70 backdrop-blur-xl border border-surface-200/60 rounded-2xl p-6 shadow-sm">
              <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
                <Terminal className="w-5 h-5 text-primary-500" />
                Initialize Task
              </h2>
              <div className="flex flex-col gap-4">
                <div className="flex flex-col gap-2">
                  <label htmlFor="goal" className="text-sm font-medium text-surface-600">
                    Agent Goal
                  </label>
                  <textarea
                    id="goal"
                    value={goal}
                    onChange={(e) => setGoal(e.target.value)}
                    placeholder="E.g., Write a comprehensive report on the future of AI agents..."
                    className="w-full bg-surface-50 border border-surface-200 rounded-xl p-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary-500/50 focus:border-primary-500 transition-all resize-none h-28"
                  />
                </div>
                <button
                  onClick={runTask}
                  disabled={status === 'pending' || status === 'running' || !goal.trim()}
                  className="w-full py-3 px-4 rounded-xl bg-gradient-to-r from-primary-600 to-indigo-600 text-white font-medium hover:shadow-lg hover:shadow-primary-500/25 transition-all focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                >
                  {(status === 'pending' || status === 'running') ? (
                    <>
                      <Loader2 className="w-4 h-4 animate-spin" />
                      Running...
                    </>
                  ) : (
                    <>
                      <Play className="w-4 h-4" />
                      Start Workflow
                    </>
                  )}
                </button>
              </div>
            </div>

            {/* Status Card */}
            <div className="bg-white/70 backdrop-blur-xl border border-surface-200/60 rounded-2xl p-6 shadow-sm flex flex-col gap-4">
               <h3 className="text-sm font-medium text-surface-500 uppercase tracking-wider">Workflow Status</h3>
               <div className="flex items-center justify-between p-4 bg-surface-50 rounded-xl border border-surface-100">
                 <div className="flex items-center gap-3">
                   {getStatusIcon()}
                   <div>
                     <p className="font-semibold text-surface-900 capitalize">{status}</p>
                     <p className="text-xs text-surface-500 font-mono">
                        {taskId ? taskId.split('-')[0] + '...' : 'No active task'}
                     </p>
                   </div>
                 </div>
               </div>
               
               {/* Progress indicator steps */}
               <div className="mt-2 space-y-3">
                 {['planner', 'researcher', 'writer_draft_1', 'reviewer_feedback_1', 'final_report'].map((step, idx) => {
                   const isDone = data?.steps?.some(s => s.step.startsWith(step.split('_')[0]));
                   return (
                     <div key={idx} className="flex items-center gap-3">
                       <div className={`w-2 h-2 rounded-full ${isDone ? 'bg-primary-500' : 'bg-surface-300'}`}></div>
                       <span className={`text-sm capitalize ${isDone ? 'text-surface-900 font-medium' : 'text-surface-400'}`}>
                         {step.replace(/_/g, ' ')}
                       </span>
                     </div>
                   );
                 })}
               </div>
            </div>
          </div>

          {/* Right Column: Terminal Logs & Output */}
          <div className="lg:col-span-2 flex flex-col gap-6">
            <div className="bg-surface-900 border border-surface-800 rounded-2xl shadow-xl overflow-hidden flex flex-col h-[600px]">
              
              <div className="bg-surface-800/50 border-b border-surface-800 px-4 py-3 flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <div className="flex gap-1.5">
                    <div className="w-3 h-3 rounded-full bg-red-500/80"></div>
                    <div className="w-3 h-3 rounded-full bg-yellow-500/80"></div>
                    <div className="w-3 h-3 rounded-full bg-green-500/80"></div>
                  </div>
                  <span className="ml-2 text-xs font-mono text-surface-400">orchestrator.log</span>
                </div>
              </div>

              <div className="flex-1 overflow-y-auto p-4 font-mono text-sm space-y-4">
                {logs.length === 0 ? (
                  <div className="text-surface-500 h-full flex items-center justify-center italic">
                    Awaiting instructions...
                  </div>
                ) : (
                  logs.map((log, idx) => (
                    <div key={idx} className="animate-in fade-in slide-in-from-bottom-2 duration-300">
                      <div className="flex items-start gap-3">
                        <span className="text-surface-500 text-xs shrink-0 mt-0.5">
                          {log.time.toLocaleTimeString([], {hour12: false})}
                        </span>
                        <div className="flex-1">
                          <span className={`
                            ${log.type === 'error' ? 'text-red-400' : ''}
                            ${log.type === 'success' ? 'text-green-400' : ''}
                            ${log.type === 'info' ? 'text-blue-400' : ''}
                            ${log.type === 'step' ? 'text-purple-400 font-semibold' : ''}
                          `}>
                            {log.msg}
                          </span>
                          {log.data && (
                            <div className="mt-2 p-3 bg-surface-950 rounded-lg overflow-x-auto border border-surface-800 text-xs leading-relaxed">
                              {renderValue(log.data)}
                            </div>
                          )}
                        </div>
                      </div>
                    </div>
                  ))
                )}
                <div ref={logsEndRef} />
              </div>
            </div>
          </div>
          
        </main>
      </div>
    </div>
  );
}

export default App;
