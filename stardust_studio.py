#!/usr/bin/env python3
"""
🌌 Stardust Studio — The Intuitive Code Alchemist's Crystallization Chamber

This single file contains the complete living system.

It does not "generate code".
It performs a controlled phase transition on human intention.

Every function, every prompt, every UI element was discovered by overlaying
three universal patterns:

- Stellar nucleosynthesis (how diffuse gas becomes a star)
- Mycelial anastomosis (how separate threads become one living network)
- Musical counterpoint (how independent voices resolve into inevitable harmony)

Run with: streamlit run stardust_studio.py

The code is deliberately monolithic yet crystalline. There are no hidden
modules because the entire act of creation must remain visible inside the
glass vessel. This is intentional emergent simplicity.
"""

from __future__ import annotations

import os
import json
import re
import tempfile
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from github import Github, GithubException
from pydantic import BaseModel, Field, ValidationError
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

# ═══════════════════════════════════════════════════════════════════════════════
#                              ALCHEMICAL CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

load_dotenv()

# Cosmic color palette (Streamlit theme hints)
st.set_page_config(
    page_title="Stardust Studio",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# The Great Work requires these constants
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")
DEFAULT_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")


# ═══════════════════════════════════════════════════════════════════════════════
#                              DATA MODELS (The Lattice)
# ═══════════════════════════════════════════════════════════════════════════════

class IntentConstellation(BaseModel):
    """The first condensation of the nebula — structured intention."""
    project_name: str = Field(..., description="Short, poetic, filesystem-safe name for the project")
    one_line_purpose: str = Field(..., description="The single sentence that contains the entire soul of the system")
    core_features: List[str] = Field(..., description="The 3-7 non-negotiable capabilities the system must possess")
    success_criteria: List[str] = Field(..., description="How we will know the crystallization succeeded")
    constraints: List[str] = Field(default_factory=list, description="Hard boundaries (tech stack, performance, philosophy)")
    vibe: str = Field(..., description="The emotional and aesthetic atmosphere the finished system should radiate")


class ArchitectureBlueprint(BaseModel):
    """The gravitational collapse has begun. The high-level structure emerges."""
    philosophy: str = Field(..., description="Why this architecture is the only one that could have been born from the intent")
    layers: List[Dict[str, Any]] = Field(..., description="Ordered layers with name, responsibility, and key patterns")
    data_flow: str = Field(..., description="How information moves through the living system (narrative form)")
    failure_modes: List[str] = Field(..., description="The elegant ways the system can fail and still remain graceful")
    growth_vectors: List[str] = Field(..., description="How the system can evolve without rewriting its soul")


class GeneratedProject(BaseModel):
    """The finished star system — ready to be born."""
    project_name: str
    files: Dict[str, str] = Field(..., description="Mapping of relative path to full file content")
    main_entry: str = Field(..., description="The command or file that starts the living system")
    run_instructions: str = Field(..., description="How a human being brings this creation to life")
    why_this_shape: str = Field(..., description="The deeper reason this particular implementation is inevitable")


# ═══════════════════════════════════════════════════════════════════════════════
#                         THE STARDUST ALCHEMIST (The Reactor Core)
# ═══════════════════════════════════════════════════════════════════════════════

class StardustAlchemist:
    """
    The living reactor.

    This class does not call an LLM.
    It performs a ritual of temperature reduction on language until
    the chaotic plasma of desire collapses into a coherent, runnable star.

    Every method corresponds to one observable phase of stellar formation.
    """

    def __init__(self, api_key: str, base_url: str = DEFAULT_BASE_URL, model: str = DEFAULT_MODEL):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        self.console = Console()  # For rich internal logging if needed

    # ──────────────────────────────────────────────────────────────────────────
    # PHASE 1: NEBULA PARSING — From gas to first solid particles
    # ──────────────────────────────────────────────────────────────────────────
    def parse_nebula(self, raw_prompt: str) -> IntentConstellation:
        """
        The prompt is still hot plasma. We apply the first structured pressure.

        This is not "extraction". It is the moment the first dust grains
        condense out of the molecular cloud.
        """
        system_prompt = """You are the Nebula Parser of Stardust Studio.

Your task is to take a raw human desire and condense it into the first crystalline
structure: an IntentConstellation.

You must think like a star forming. The output must feel INEVITABLE — as if
this particular constellation of features, constraints, and vibe could not have
been otherwise given the prompt.

Respond ONLY with valid JSON matching the IntentConstellation schema.
Do not add commentary. The JSON is the first act of creation."""

        user_prompt = f"Raw human desire (the nebula):\n\n{raw_prompt}\n\nCondense this into the first IntentConstellation."

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.4,  # Cool enough for structure, warm enough for creativity
        )

        content = response.choices[0].message.content
        data = json.loads(content)
        return IntentConstellation(**data)

    # ──────────────────────────────────────────────────────────────────────────
    # PHASE 2: CONSTELLATION DESIGN — Gravitational collapse into architecture
    # ──────────────────────────────────────────────────────────────────────────
    def design_constellation(self, intent: IntentConstellation) -> ArchitectureBlueprint:
        """
        The dust has clumped. Now gravity takes over.

        We design the architecture not as boxes and arrows, but as a living
        gravitational system whose shape is dictated by the intent's mass distribution.
        """
        system_prompt = """You are the Constellation Architect of Stardust Studio.

You receive an IntentConstellation and must design the only architecture
that could naturally emerge from it.

Rules of emergence:
- Every layer must have a clear physical or biological metaphor.
- The data flow must read like a story of transformation.
- Failure modes must be graceful, almost beautiful.
- Growth vectors must feel like natural evolution, not bolted-on features.

Respond ONLY with valid JSON matching the ArchitectureBlueprint schema.
The philosophy field should read like a short cosmological observation."""

        user_prompt = f"""Intent Constellation (the mass that dictates gravitational collapse):

{intent.model_dump_json(indent=2)}

Design the inevitable architecture that must form around this intent."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.3,
        )

        data = json.loads(response.choices[0].message.content)
        return ArchitectureBlueprint(**data)

    # ──────────────────────────────────────────────────────────────────────────
    # PHASE 3 + 4: FRAGMENT CRYSTALLIZATION + HARMONIC INTEGRATION
    # We do these together because true emergence happens when fragments
    # are grown while already knowing they must eventually sing in harmony.
    # ──────────────────────────────────────────────────────────────────────────
    def crystallize_and_harmonize(
        self, intent: IntentConstellation, blueprint: ArchitectureBlueprint
    ) -> GeneratedProject:
        """
        The most sacred phase.

        Here we grow every file as a crystal while simultaneously ensuring
        that every crystal knows about every other crystal's existence and
        resonance frequency.

        This is mycelial + fugue at once.
        """
        system_prompt = f"""You are the Crystal Grower and Harmonic Weaver of Stardust Studio.

You have received:
1. An IntentConstellation — the soul of what must exist.
2. An ArchitectureBlueprint — the gravitational skeleton.

Your task is to grow a COMPLETE, PRODUCTION-GRADE, BEAUTIFUL software system
that feels like it was discovered rather than constructed.

MANDATORY RULES OF CRYSTALLIZATION:
- Every file must contain a short "Why this shape exists" comment or docstring
  written in the language of physics, biology, or music.
- The code must be elegant enough that a senior engineer would say "of course".
- Include a beautiful README.md that tells the story of this system's birth.
- Include requirements.txt or pyproject.toml.
- Include at least one meaningful test (pytest preferred).
- The main entry point must be obvious and delightful to run.
- Use modern Python (3.10+), type hints, and clean error handling.
- The entire project must be runnable with 3 commands after cloning.

OUTPUT FORMAT:
Return ONLY a single JSON object with this exact structure:
{{
  "project_name": "...",
  "files": {{
    "README.md": "full markdown content...",
    "src/main.py": "full code...",
    ...
  }},
  "main_entry": "python -m src.main or ./run.sh or streamlit run app.py",
  "run_instructions": "Clear, poetic, step-by-step instructions a human can follow in under 60 seconds.",
  "why_this_shape": "A profound paragraph explaining why this exact implementation is the only one that could have emerged from the intent and blueprint."
}}

The 'files' dictionary must contain every file needed for a complete, clone-and-run experience.
No placeholders. No TODOs. No missing imports. The system must actually work."""

        user_prompt = f"""INTENT CONSTELLATION:
{intent.model_dump_json(indent=2)}

ARCHITECTURE BLUEPRINT:
{blueprint.model_dump_json(indent=2)}

Now grow the complete living system. Every crystal must already know the song it will sing with its siblings."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.5,  # Slightly warmer — crystals have personality
            max_tokens=16000,  # Generous for full projects
        )

        data = json.loads(response.choices[0].message.content)
        return GeneratedProject(**data)

    # ──────────────────────────────────────────────────────────────────────────
    # PHASE 5: RESONANCE TESTING — The vacuum chamber
    # ──────────────────────────────────────────────────────────────────────────
    def test_resonance(self, project: GeneratedProject) -> Tuple[bool, List[str]]:
        """
        We place the newborn star in vacuum and watch how it vibrates.

        This is not comprehensive testing. It is a resonance check —
        does the system ring true when struck?
        """
        issues: List[str] = []

        # Basic structural resonance
        if not project.files:
            issues.append("No files crystallized — the nebula never cooled.")

        required_roots = {"README.md", "requirements.txt", "pyproject.toml"}
        present_roots = {Path(p).name for p in project.files}
        if not required_roots & present_roots:
            issues.append("Missing foundational files (README or dependency manifest). The star has no surface.")

        # Try to detect obvious Python syntax fractures in .py files
        for path, content in project.files.items():
            if path.endswith(".py"):
                try:
                    compile(content, path, "exec")
                except SyntaxError as e:
                    issues.append(f"Syntax fracture in {path}: {e}")

        is_resonant = len(issues) == 0
        return is_resonant, issues

    # ──────────────────────────────────────────────────────────────────────────
    # PHASE 6: SUPERNOVA RELEASE — The stellar wind
    # ──────────────────────────────────────────────────────────────────────────
    def release_supernova(
        self,
        project: GeneratedProject,
        github_token: Optional[str] = None,
        new_repo_name: Optional[str] = None,
        private: bool = True,
    ) -> Dict[str, Any]:
        """
        The star is complete. Now we decide whether to keep it in the local
        cluster or release it into the wider galaxy via GitHub.

        This method can:
        - Write the project to a local directory
        - Create a new GitHub repository and push everything in one commit
        """
        result: Dict[str, Any] = {"local_path": None, "github_url": None, "success": False}

        # Always materialize locally first (in /tmp for safety)
        safe_name = re.sub(r"[^a-zA-Z0-9_-]", "-", project.project_name).lower()
        local_dir = Path(tempfile.mkdtemp(prefix=f"stardust_{safe_name}_"))
        for rel_path, content in project.files.items():
            full_path = local_dir / rel_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content, encoding="utf-8")

        result["local_path"] = str(local_dir)

        # Optional: Release to GitHub
        if github_token and new_repo_name:
            try:
                g = Github(github_token)
                user = g.get_user()
                repo = user.create_repo(
                    name=new_repo_name,
                    description=project.one_line_purpose if hasattr(project, 'one_line_purpose') else "A star born in Stardust Studio",
                    private=private,
                    auto_init=False,
                )

                # Push all files in a single commit
                for rel_path, content in project.files.items():
                    repo.create_file(
                        path=rel_path,
                        message=f"✨ Birth of {project.project_name} — crystallized in Stardust Studio",
                        content=content,
                        branch="main",
                    )

                result["github_url"] = repo.html_url
                result["success"] = True
            except GithubException as e:
                result["github_error"] = str(e)
                result["success"] = False

        return result


# ═══════════════════════════════════════════════════════════════════════════════
#                              THE GLASS CHAMBER (Streamlit UI)
# ═══════════════════════════════════════════════════════════════════════════════

def get_alchemist() -> StardustAlchemist:
    """Retrieve or create the alchemist instance from session state."""
    if "alchemist" not in st.session_state:
        api_key = os.getenv("OPENAI_API_KEY")
        base_url = os.getenv("OPENAI_BASE_URL", DEFAULT_BASE_URL)
        model = os.getenv("OPENAI_MODEL", DEFAULT_MODEL)

        if not api_key:
            st.error("No OPENAI_API_KEY found in environment. Please set it in .env or sidebar.")
            st.stop()

        st.session_state.alchemist = StardustAlchemist(api_key=api_key, base_url=base_url, model=model)
    return st.session_state.alchemist


def render_cosmic_header():
    """The entrance to the chamber."""
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0 1rem 0;">
        <h1 style="font-size: 3.5rem; margin-bottom: 0.2rem;">🌌 Stardust Studio</h1>
        <p style="font-size: 1.3rem; color: #9aa0a6; margin-top: 0;">The Intuitive Code Alchemist</p>
        <p style="max-width: 620px; margin: 1rem auto; color: #6b7280;">
            From raw desire → structured intention → living, breathing software.<br>
            One click. One phase transition. One new star in the cosmos.
        </p>
    </div>
    """, unsafe_allow_html=True)


def main():
    render_cosmic_header()

    # ── Sidebar: The Control Panel of the Chamber ─────────────────────────────
    with st.sidebar:
        st.header("⚙️ Chamber Controls")

        st.markdown("**LLM Provider**")
        model = st.text_input("Model", value=os.getenv("OPENAI_MODEL", DEFAULT_MODEL), key="model")
        base_url = st.text_input("Base URL", value=os.getenv("OPENAI_BASE_URL", DEFAULT_BASE_URL), key="base_url")

        st.divider()

        st.markdown("**GitHub Release** (for generated products)")
        github_token = st.text_input(
            "GitHub Token (repo scope)",
            value=os.getenv("GITHUB_TOKEN", ""),
            type="password",
            key="github_token"
        )
        github_username = st.text_input(
            "GitHub Username",
            value=os.getenv("GITHUB_USERNAME", ""),
            key="github_username"
        )

        st.divider()
        st.caption("The chamber is transparent. All prompts and reasoning are visible in the process.")

    # ── Main Chamber ──────────────────────────────────────────────────────────
    alchemist = get_alchemist()

    # The Prompt — raw stardust
    st.subheader("Enter the Raw Nebula (Your Desire)")
    raw_prompt = st.text_area(
        label="Describe the software you want to exist in the universe",
        height=140,
        placeholder="A beautiful, local-first habit tracker that feels like a garden you tend every morning. It should use rich terminal UI, store data in a single JSON file, support gentle streaks, and never feel like work.",
        key="raw_prompt"
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        transmute_clicked = st.button("✨ Transmute Prompt → Living Product", type="primary", use_container_width=True)

    if not transmute_clicked:
        st.info("The nebula awaits your observation. Enter a desire above and click the button to begin the phase transition.")
        st.stop()

    # ═══════════════════════════════════════════════════════════════════════
    #                    THE GREAT WORK — THE SIX PHASES
    # ═══════════════════════════════════════════════════════════════════════

    if "generated_project" not in st.session_state:
        st.session_state.generated_project = None

    with st.status("🌌 Beginning controlled phase transition...", expanded=True) as status:

        # PHASE 1
        st.write("**Phase 1 — Nebula Parsing** — Condensing plasma into first dust grains...")
        try:
            intent = alchemist.parse_nebula(raw_prompt)
            st.success(f"Intent crystallized: **{intent.project_name}** — {intent.one_line_purpose}")
            with st.expander("View Intent Constellation (first solid structure)"):
                st.json(intent.model_dump())
        except Exception as e:
            st.error(f"Nebula failed to condense: {e}")
            status.update(label="Phase transition failed at nebula stage", state="error")
            st.stop()

        time.sleep(0.6)

        # PHASE 2
        st.write("**Phase 2 — Constellation Design** — Gravity organizes the dust into structure...")
        try:
            blueprint = alchemist.design_constellation(intent)
            st.success("Architecture has gravitationally collapsed into coherent form.")
            with st.expander("View Architecture Blueprint"):
                st.json(blueprint.model_dump())
        except Exception as e:
            st.error(f"Gravitational collapse failed: {e}")
            status.update(label="Phase transition failed at architecture stage", state="error")
            st.stop()

        time.sleep(0.6)

        # PHASE 3+4
        st.write("**Phase 3+4 — Crystallization & Harmonic Integration** — Growing and weaving all fragments into one living mycelium...")
        try:
            project = alchemist.crystallize_and_harmonize(intent, blueprint)
            st.success(f"Star system fully formed: **{project.project_name}**")
            with st.expander("View Generated Project Metadata"):
                st.json(project.model_dump(exclude={"files"}))
        except Exception as e:
            st.error(f"Crystallization failed: {e}")
            status.update(label="Crystallization failed", state="error")
            st.stop()

        time.sleep(0.6)

        # PHASE 5
        st.write("**Phase 5 — Resonance Testing** — Placing the newborn in vacuum chamber...")
        is_resonant, issues = alchemist.test_resonance(project)
        if is_resonant:
            st.success("The system rings true. No fractures detected.")
        else:
            st.warning("Resonance issues detected (non-fatal for demo):")
            for issue in issues:
                st.write(f"• {issue}")

        time.sleep(0.4)

        # Store for later use
        st.session_state.generated_project = project
        st.session_state.intent = intent
        st.session_state.blueprint = blueprint

        status.update(label="✨ Phase transition complete. A new star has been born.", state="complete")

    # ═══════════════════════════════════════════════════════════════════════
    #                        THE BORN STAR — PREVIEW & RELEASE
    # ═══════════════════════════════════════════════════════════════════════

    st.divider()
    st.header(f"🌟 {project.project_name}")
    st.markdown(f"*{project.why_this_shape}*")

    # File tree + content preview
    st.subheader("The Crystallized Lattice (All Files)")

    # Simple but elegant file browser
    file_names = sorted(project.files.keys())
    selected_file = st.selectbox("Select a file to inspect its crystalline structure", file_names, index=0)

    if selected_file:
        content = project.files[selected_file]
        lang = "python" if selected_file.endswith((".py", ".pyi")) else "markdown" if selected_file.endswith(".md") else "json" if selected_file.endswith(".json") else "text"
        st.code(content, language=lang, line_numbers=True)

    # Run instructions
    st.subheader("How to Awaken This Star")
    st.code(project.run_instructions, language="bash")

    # Release controls
    st.divider()
    st.subheader("Release the Star into the Cosmos")

    release_col1, release_col2 = st.columns(2)

    with release_col1:
        if st.button("💾 Materialize Locally (in /tmp)", use_container_width=True):
            result = alchemist.release_supernova(project)
            st.success(f"Star materialized at: `{result['local_path']}`")
            st.caption("You can now cd into it and follow the run instructions.")

    with release_col2:
        repo_name_input = st.text_input(
            "New GitHub Repository Name",
            value=re.sub(r"[^a-zA-Z0-9-]", "-", project.project_name).lower()[:80],
            key="new_repo_name"
        )
        private_repo = st.checkbox("Private repository", value=True)

        if st.button("🚀 Release to GitHub (creates new repo + pushes)", type="primary", use_container_width=True):
            if not github_token:
                st.error("GitHub token required in sidebar or .env to release to GitHub.")
            else:
                with st.spinner("Releasing stellar wind... creating repo and pushing all crystals..."):
                    result = alchemist.release_supernova(
                        project,
                        github_token=github_token,
                        new_repo_name=repo_name_input,
                        private=private_repo,
                    )
                    if result.get("github_url"):
                        st.success(f"Star released! View it here: {result['github_url']}")
                        st.balloons()
                    else:
                        st.error(f"Release failed: {result.get('github_error', 'Unknown error')}")

    # Final philosophical note
    st.divider()
    st.caption("""
    This system was not assembled. It was allowed to form.
    Every line you see above emerged because the metaphors were strong enough
    to guide the model toward beauty rather than complexity.
    """)


if __name__ == "__main__":
    main()