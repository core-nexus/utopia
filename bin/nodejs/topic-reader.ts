#!/usr/bin/env node

import { readFileSync } from 'fs';
import { resolve } from 'path';

function getTopicContent(topicSlug: string): string {
  const topicPath = resolve(process.cwd(), '../../topics', topicSlug, 'topic.md');
  
  try {
    const content = readFileSync(topicPath, 'utf-8');
    
    // Find the end of frontmatter (second occurrence of ---)
    const lines = content.split('\n');
    let frontmatterEnd = -1;
    let frontmatterCount = 0;
    
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].trim() === '---') {
        frontmatterCount++;
        if (frontmatterCount === 2) {
          frontmatterEnd = i;
          break;
        }
      }
    }
    
    if (frontmatterEnd === -1) {
      // No frontmatter found, return entire content
      return content.trim();
    }
    
    // Return content after frontmatter
    return lines.slice(frontmatterEnd + 1).join('\n').trim();
  } catch (error) {
    console.error(`Error reading topic file: ${topicPath}`);
    process.exit(1);
  }
}

// CLI usage
if (import.meta.url === `file://${process.argv[1]}`) {
  const topicSlug = process.argv[2];
  
  if (!topicSlug) {
    console.error('Usage: topic-reader.ts <topic-slug>');
    process.exit(1);
  }
  
  const content = getTopicContent(topicSlug);
  console.log(content);
}

export { getTopicContent };