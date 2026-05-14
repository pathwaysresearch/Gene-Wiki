# Week 4 - Video 3-  Discrimination / Bias

**Channel:** M. Iftikhar Uddin Khan Sami   |   **Date:** 2020-05-16   |   **URL:** https://www.youtube.com/watch?v=1bGNzboXaD0

## Description

AI is not only for engineers. If you want your organization to become better at using AI, this is the course to tell everyone--especially your non-technical colleagues--to take. 

In this course, you will learn:

- The meaning behind common AI terminology, including neural networks, machine learning, deep learning, and data science
- What AI realistically can--and cannot--do
- How to spot opportunities to apply AI to problems in your own organization
- What it feels like to build machine learning and data science projects
- How to work with an AI team and build an AI strategy in your company
- How to navigate ethical and societal discussions surrounding AI

Though this course is largely non-technical, engineers can also take this course to learn the business aspects of AI.

## Transcript

Andrew Ng: How does an AI system become biased and therefore discriminate against some people, and how can we try to reduce or eliminate this effect in our AI systems? Let's start with an example.

Andrew Ng: A group at Microsoft found this remarkable result that when AI learns from text found on the internet, it can learn unhealthy stereotypes. To their credit, they also proposed technical solutions for reducing the amount of bias in this type of AI system. Here's what they found. By having an AI read text on the internet, it can learn about words and you can ask it to reason about analogies. So you can quiz the AI system, now that you've read all this text on the internet, in the analogy, Man is to Woman as Father is to what?

Andrew Ng: So the AI will output the word mother, which reflects the way these words are typically used on the internet. If you ask it, Man is to Woman as King is to what? Then the same AI system will say, as King is to Queen, which again seems reasonable relative to the way these words are used on the internet. The researchers also found the following result, which is that if you ask it, Man is to Computer programmer as Woman is to what? that the same AI system would output the answer, Woman is to Homemaker. And I think this answer is really unfortunate. A less biased answer would be if we were to say, Woman is to computer programmer.

Andrew Ng: If we want our AI system to understand that men and women can equally be computer programmers, just as men and women can equally be homemakers, then we would like it to output man is a computer programmer as woman is computer programmer, and also man is a homemaker as woman is a homemaker.

Andrew Ng: How does an AI system learn to become biased like this from data? Let's dive a bit more into the technical details.

Andrew Ng: The way an AI system stores words is using a set of numbers. So let's say the word man is stored or we sometimes say represented as the two numbers 1, 1. The way an AI system comes up with these numbers is through statistics of how the word man is used on the internet. The specific process for how these numbers are computed is quite complex and I won't go into that here, but these numbers represent the typical usage of these words. In practice, an AI might have hundreds or thousands of numbers to store a word, but I'm just going to use two numbers here to keep the example simpler. Let me take this number and plot it on a chart. So the word man I'm going to plot at the position 1, 1 on the figure on the right.

Andrew Ng: By looking at the statistics of how the words or how the phrase computer programmer is used on the internet, the AI will have a different pair of numbers, say 3, 2, to store or to represent the phrase computer programmer. And similarly, by looking at how the word women is used, it will come up with a different pair of numbers, say 2, 3, to store or to represent the word women.

Andrew Ng: When you ask the AI system to compute the analogy above, Man is to computer programmer as woman is to what? Then what the AI system will do is construct a parallelogram that looks like this, and it will ask what is the word associated with the position 4, 4, because it will think that is the answer to this analogy. One way to think about this mathematically is that the AI thinks the relationship of man to computer programmer is that you start from the word man, go two steps to the right and one step up. And so to find the same answer for woman is to what, you would also go two steps to the right and one step up.

Andrew Ng: Unfortunately, when these numbers are derived from text on the internet, an AI system finds that the way the word homemaker is used on the internet causes it to be placed at the position 4, 4, which is why the AI system comes up with this biased analogy.

Andrew Ng: AI systems are already making important decisions today and will continue to do so in the future as well. So, bias matters. For example, there's a company that was using AI for hiring and found that their hiring tool discriminated against women. This is clearly unfair, and so this company shut down their tool.

Andrew Ng: Second, there are also some facial recognition systems that seem to work more accurately for light-skinned than dark-skinned individuals. If an AI system is trained primarily on data of lighter-skinned individuals, then it will be more accurate for that category of individuals. To the extent that these systems are used in, for example, criminal investigations, this can create a very biased and unfair effect for dark-skinned individuals. So many face recognition teams today are working hard to ensure that the systems do not exhibit this type of bias.

Andrew Ng: There have also been AI or statistical loan approval systems that wound up discriminating against some minority ethnic groups and quoted them a higher interest rate. Banks have also been working to make sure to diminish or eliminate this type of bias in their approval systems.

Andrew Ng: Finally, I think it's important that AI systems do not contribute to the toxic effect of reinforcing unhealthy stereotypes. For example, if an 8-year-old girl goes to an image search engine and searches for chief executive officer, if they see only pictures of men, or if they see no one that looks like themselves, either by gender or ethnicity, we don't want them to be discouraged from pursuing a career that might lead her to someday be a chief executive officer of a large company.

Andrew Ng: Because of these issues, the AI community has put a lot of effort into combating bias. For example, we're starting to have better and better technical solutions for reducing bias in AI systems. In the example you saw at the start of this video of the AI outputting biased analogies, simplifying the description a little bit, researchers have found that when an AI system learns a lot of different numbers with which to store words, there are a few numbers that correspond to the bias, and if you zero out those numbers, just set them to zero, then the bias diminishes significantly.

Andrew Ng: A second solution is to try to use less biased and/or more inclusive data. For example, if you are building a face recognition system and make sure to include data from multiple ethnicities and all genders, then your system will be less biased and more inclusive. Second, many AI teams are subjecting their systems to better transparency and/or auditing processes so that we can constantly check what types of bias, if any, these AI systems are exhibiting so that we can at least recognize the problem if it exists and then take steps to address it. For example, many face recognition teams are systematically checking how accurate their system is on different subsets of the population to check whether it is more or less accurate on dark-skinned versus light-skinned individuals, for example. Having transparent systems as well as systematic auditing processes increases the odds that we'll at least quickly spot a problem in case there is one so we can fix it.

Andrew Ng: Finally, I think having a diverse workforce will also help reduce bias. If you have a diverse workforce, then the individuals at your workforce are more likely to be able to spot different problems and maybe that will help make your data more diverse and more inclusive in the first place. By having more unique points of view as you're building AI systems, I think this will help all of us create less biased applications.

Andrew Ng: AI systems are making really important decisions today, and so their bias or potential for bias is something we must pay attention to and work to diminish. One thing that makes me optimistic about this is that we actually have better ideas today for reducing bias in AI than reducing bias in humans. So while we should never be satisfied until all AI bias is gone, and it will take us quite a bit of work to get there, I'm also optimistic if we could take AI systems that started off with a level similar to humans because it learned from humans, and we can cut down the bias from there through technical solutions or other means so that as a society, we can hopefully make the decisions we're making through humans or through AI rapidly become more fair and less biased.

Andrew Ng: In addition to the problem of bias, one of the other limitations of AI is that it can be open to adversarial attacks. In the next video, you'll learn what are adversarial attacks as well as some of the things you could do to guard against them. Let's go on to the next video.