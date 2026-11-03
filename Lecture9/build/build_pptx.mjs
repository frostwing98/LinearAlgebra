import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";

const workspaceDir = "C:\\Github\\LinearAlgebra";
const skillDir = "C:\\Users\\Allen\\.codex\\plugins\\cache\\openai-primary-runtime\\presentations\\26.1029.11837\\skills\\presentations";
const artifactToolPath = "C:\\Users\\Allen\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\node\\node_modules\\@oai\\artifact-tool\\dist\\artifact_tool.mjs";
const pythonExecutable = "C:\\Users\\Allen\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe";
process.env.RUNTIME_NODE_MODULES = "C:\\Users\\Allen\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\node\\node_modules";
const renderDir = path.join(workspaceDir, "Lecture9", "build", "render");
const stagingDir = path.join(workspaceDir, "Lecture9", "build", ".codex-finalizer");
const finalPath = path.join(workspaceDir, "Lecture9", "output", "MATH100_Lecture9_Determinants_and_Midterm_Solutions.pptx");

const { Presentation, PresentationFile } = await import(pathToFileURL(artifactToolPath).href);
const { finalizePresentation } = await import(pathToFileURL(
  path.join(skillDir, "container_tools", "artifact_tool_utils.mjs"),
).href);

const imageNames = (await fs.readdir(renderDir))
  .filter((name) => /^slide-\d+\.png$/i.test(name))
  .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));

if (imageNames.length !== 54) {
  throw new Error(`Expected 54 rendered pages, found ${imageNames.length}`);
}

const presentation = Presentation.create({
  slideSize: { width: 1280, height: 720 },
});

for (const imageName of imageNames) {
  const slide = presentation.slides.add();
  slide.background.fill = "#FFFFFF";
  const imageBytes = await fs.readFile(path.join(renderDir, imageName));
  slide.images.add({
    blob: imageBytes.buffer.slice(
      imageBytes.byteOffset,
      imageBytes.byteOffset + imageBytes.byteLength,
    ),
    contentType: "image/png",
    alt: `Lecture 9 slide ${imageName.match(/\d+/)[0]}`,
    fit: "cover",
    position: { left: 0, top: 0, width: 1280, height: 720 },
  });
}

await fs.mkdir(stagingDir, { recursive: true });
await fs.mkdir(path.dirname(finalPath), { recursive: true });
const candidatePath = path.join(stagingDir, "candidate.pptx");
await (await PresentationFile.exportPptx(presentation)).save(candidatePath);

const result = await finalizePresentation({
  explicitTotalSlideCount: 54,
  requiredNativeTableOwnerSlides: [],
  requiredNativeChartOwnerSlides: [],
  workspaceDir,
  candidatePath,
  finalPath,
  pythonExecutable,
  integrityValidatorPath: path.join(skillDir, "container_tools", "inspect_presentation_package_integrity.py"),
  layoutValidatorPath: path.join(skillDir, "container_tools", "inspect_presentation_layout_geometry.py"),
  layoutArgs: [
    "--expected-slide-size-emu", "12192000,6858000",
    "--validate-heading-fit",
  ],
  verifyArtifactToolImport: true,
  receiptPath: path.join(stagingDir, "lecture9.validation.json"),
});

console.log(JSON.stringify({ finalPath, slideCount: imageNames.length, result }, null, 2));
