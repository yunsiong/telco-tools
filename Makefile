all: telco_tools/fs_agent.js telco_tools/tracer_agent.js telco_tools/itracer_agent.js

telco_tools/fs_agent.js: agents/fs/agent.ts
	cd agents/fs && npm install && npm run build

telco_tools/tracer_agent.js: agents/tracer/agent.ts
	cd agents/tracer && npm install && npm run build

telco_tools/itracer_agent.js: agents/itracer/agent.ts
	cd agents/itracer && npm install && npm run build

.PHONY: all
