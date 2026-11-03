import fs from "node:fs/promises";
import { pathToFileURL } from "node:url";

const artifactToolPath = "C:\\Users\\Allen\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\node\\node_modules\\@oai\\artifact-tool\\dist\\artifact_tool.mjs";
const finalPath = "C:\\Github\\LinearAlgebra\\Lecture9\\output\\MATH100_Lecture9_Determinants_and_Midterm_Solutions.pptx";
const outputDir = "C:\\Github\\LinearAlgebra\\Lecture9\\build\\final-render";
const { FileBlob, PresentationFile } = await import(pathToFileURL(artifactToolPath).href);

await fs.mkdir(outputDir, { recursive: true });
const presentation = await PresentationFile.importPptx(await FileBlob.load(finalPath));
const montage = await presentation.export({ format: "webp", montage: true });
await fs.writeFile(`${outputDir}\\montage.webp`, new Uint8Array(await montage.arrayBuffer()));

for (const slideNumber of [1, 8, 24, 44, 53, 54]) {
  const slide = presentation.slides.items[slideNumber - 1];
  const png = await presentation.export({ slide, format: "png", scale: 1 });
  await fs.writeFile(
    `${outputDir}\\slide-${String(slideNumber).padStart(2, "0")}.png`,
    new Uint8Array(await png.arrayBuffer()),
  );
}

console.log(JSON.stringify({ slideCount: presentation.slides.items.length, outputDir }));
