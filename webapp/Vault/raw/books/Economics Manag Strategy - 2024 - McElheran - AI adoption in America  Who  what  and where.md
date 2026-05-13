

[Page 1]
Received: 22 June 2022
Revised: 1 September 2023 Accepted: 28 October 2023
DOI: 10.1111/jems.12576

SPECIAL ISSUE ARTICLE

[IMAGE: Check for updates link] Check for updates

[IMAGE: Journal of Economics & Management Strategy logo] Journal of Economics & Management Strategy [IMAGE: WILEY logo] WILEY

# AI adoption in America: Who, what, and where

**Kristina McElheran¹ | J. Frank Li² | Erik Brynjolfsson³ | Zachary Kroff⁴ | Emin Dinlersoz⁴ | Lucia Foster⁴ | Nikolas Zolas⁴**

¹UTSC and Rotman School of Management, University of Toronto, Toronto, Ontario, Canada

²Sauder School of Business, University of British Columbia, Vancouver, British Columbia, Canada

³Stanford Digital Economy Lab, Stanford University, Stanford, California, USA

⁴Center for Economic Studies, U.S. Census Bureau, Suitland-Silver Hill, Maryland, USA

**Correspondence**
Kristina McElheran, UTSC and Rotman School of Management, University of Toronto, Toronto, ON, Canada.
Email: k.mcelheran@utoronto.ca

**Funding information**
Ewing Marion Kauffman Foundation; Social Sciences and Humanities Research Council of Canada

> **Abstract**
> We study the early adoption and diffusion of five artificial intelligence (AI)- related technologies (automated-guided vehicles, machine learning, machine vision, natural language processing, and voice recognition) as documented in the 2018 Annual Business Survey of 850,000 firms across the United States. We find that fewer than 6% of firms used any of the AI-related technologies we measure, though most very large firms reported at least some AI use. Weighted by employment, average adoption was just over 18%. AI use in production, while varying considerably by industry, was found in every sector of the economy and clustered with emerging technologies, such as cloud computing and robotics. Among dynamic young firms, AI use was highest alongside more-educated, more-experienced, and younger owners, including owners motivated by bringing new ideas to market or helping the community. AI adoption was also more common in startups displaying indicators of high- growth entrepreneurship, including venture capital funding, recent product and process innovation, and growth-oriented business strategies. Early AI adoption was far from evenly distributed: a handful of “superstar" cities and emerging hubs led startups' adoption of AI. These patterns of early AI use foreshadow economic and social impacts far beyond this limited initial diffusion, with the possibility of a growing “AI divide” if early patterns persist.

# 1 | INTRODUCTION

Artificial intelligence (AI) may spark a revolution in business and the economy (Spulber, 2011b). However, systematic evidence on who the using firms are, what types of business they are in, or where they are located, has been slow to accumulate. This makes it difficult to understand AI's economic and managerial implications or ground predictions in objective data. Yet, the consequences of uninformed Al investment and policy may be far-reaching (Agrawal et al., 2019). To address this, we leverage new large-scale survey data to characterize early AI use across the US economy, surfacing factors with the potential to shape its impact on workers, firms, and society.

Organizational contexts are well known to influence technology use and its outcomes (Bresnahan et al., 2002), including, more recently, advances in data analytics (Brynjolfsson, Jin, et al., 2021; Wu et al., 2020). Today, apprehension is growing over the contexts and consequences of rapidly advancing innovations. Income inequality is rising, with evidence tracing this to digitization (Autor et al., 2020; Barth et al., 2023). AI-related technologies, in

---
This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made.
© 2024 The Authors. Journal of Economics & Management Strategy published by Wiley Periodicals LLC.

J Econ Manage Strat. 2024;33:375–415.

wileyonlinelibrary.com/journal/jems

375

[Page 2]
particular, are attracting debate (Acemoglu & Restrepo, 2020; Brynjolfsson, 2022). Yet, limited insight into the
industrial and organizational details surrounding their use limits guidance regarding specific areas of promise or
concern.

To shed light on the use of AI by firms, we rely on a new nationally representative survey, the Annual Business
Survey (ABS), conducted jointly between the US Census Bureau and the National Center for Science and Engineering
Statistics (NCSES) within the National Science Foundation. The ABS solicits information on firm-level use of several
advanced technologies—including those currently associated with progress in AI—over the prior year, beginning in
2018. The initial wave of the survey was sent to a large, representative sample of over 850,000 firms in the private
nonfarm economy, with a high response rate of 69%.¹ We link this to the Longitudinal Business Database (LBD), which
provides a panel of administrative data on employment and revenue throughout the firm life cycle for a near-universe
of US firms. This allows us to characterize early AI use in a sample of 447,000 firms that, once weighted appropriately,
is representative of over 4 million firms nationwide. We further leverage rich founder and organizational data for a
subsample of 75,000 startups to provide insight into the relationship between AI use and firm dynamics.

We first analyze who adopted AI, defined as a firm's use of at least one AI-related technology in production.² Our
representative data indicate that just under 6% of firms nationwide used AI as of 2017. Yet most very large firms (over
5,000 employees), reported at least some AI use. Employment-weighted adoption was just over 18%. Intensity varied
from merely testing (1.1%) to using AI in more than a quarter of production (2.2%). More-intensive use was more
prevalent among very large firms. Manufacturing and information were leading sectors, with adoption rates of roughly
12% each. Yet the breadth of AI's potential is evident in its presence across every sector of the US economy, as well as in
the diversity of its applications.

Our ability to observe *what* was adopted, in terms of specific business technologies (including, but not limited to,
AI), reveals key interdependencies. Firms using AI relied more on both digitized information and cloud computing,
suggesting important complementarities with other “enabling” technologies (Bresnahan & Trajtenberg, 1995; Goldfarb
et al., 2023). Also, while typically studied in isolation, AI and robotics overlap: most firms using robotics in production
also used AI. This clustering of emerging technologies points to mutually reinforcing technical and process innovation,
which tend to promote broader economic impact over time (Goldfarb et al., 2023; Rosenberg, 1963).

Visibility to the firm life cycle in the LBD reveals that, conditional on size and industry, younger firms were more
likely to use AI. Given the central role of young firms in innovation and economic dynamism (e.g., Acemoglu
et al., 2018; Decker et al., 2017; Haltiwanger et al., 2013; Spulber, 2011a), we expect that patterns of AI adoption among
growth- and innovation-oriented startups will be essential to understanding the rate and direction of AI use in the
economy, moving forward.

We thus delve into a large subsample of startups (around 75,000 firms 5 years old or younger) for which we have
exceptionally detailed data on owner characteristics and motivations, startup financing, as well as innovation and
business strategies. We find that AI-using startups tended to have younger, yet more-educated and more-experienced,
leaders. Founders motivated to bring new ideas to market and help the community were more prevalent among AI
users than those pursuing so-called “lifestyle” entrepreneurship (emphasizing flexible hours or work-family balance).
Markers of high-growth entrepreneurship, such as venture capital (VC) funding, high initial capitalization, and
reliance on formal intellectual property (IP), also predict AI use. Recent innovation in products or processes was also
strongly associated with AI use, as were growth-oriented business strategies.

We argue that these differences—many determined at founding (Guzman & Stern, 2015, 2016) or suggesting
distinct strategic commitments (Ghemawat, 1991; Li, 2023; McElheran et al., 2019)—are fundamental to understanding
AI's trajectory. Further, while markers of high-growth potential (Azoulay et al., 2020; Guzman & Stern, 2020) predict
AI use, conditioning on them reduces but does not eliminate a significant association between AI use and revenue
growth. This holds for later revenue growth, too, in a sample that includes older firms. While establishing causality is
beyond the reach of our data, these findings point to linkages between AI use and firm performance.³

Finally, while the spread of AI use across the country remains in its initial phase, the potential for an “AI divide”
across regions and cities is attracting concern. Thus, we also explore where early AI adoption was located, finding the
geography of AI use among startups, in particular, to be quite concentrated. While the expected influence of
California's Silicon Valley and Bay Area is apparent, the share of startups using AI is also high in metro areas
surrounding Nashville, San Antonio, Las Vegas, New Orleans, San Diego, and Tampa. Once we weight by employment
to account for worker exposure to AI, Riverside, Louisville, Columbus, Austin, and Atlanta also show concentrated AI
use. This distinction between firm adoption and employee exposure may be critical to assessing the “future of work”
across these locales. Specifically, our approach flags a number of emerging hubs for AI use that are distinct from those

[Page 3]
associated with early invention and commercialization of AI-related technologies (e.g., Bessen et al., 2021; Muro & Liu, 2021).

This rich snapshot of early AI use constitutes the most extensive and detailed evidence on actual AI use, to date. Our main objective is to document—rather than explain—a number of new stylized facts. Taken together, they point to numerous organizational and geographic intangibles that have already begun to shape AI use in ways that have been largely unobserved.

Yet these patterns of early use signpost where AI is likely to have the most (or at least the earliest-observable) impact. For example, the strong connection of AI use to process innovation highlights a classic friction that must be overcome for a new technology's potential to be seen in economic and organizational outcomes (Bresnahan & Greenstein, 1996; Feigenbaum & Gross, 2021; McElheran, 2015). AI use alongside prosocial founding motivations may provide guardrails against unethical or biased applications (Cowgill & Tucker, 2020), while concentration among large incumbents may augment existing “superstar" firm dynamics (Autor et al., 2020; Bresnahan, 2019; Camuffo et al., 2023; Tambe et al. 2020). Geographic concentration further evokes concerns about an AI-fueled "digital divide," if such patterns persist.

Much work remains to unpack these and other implications of our findings. They illustrate, however, numerous ways in which future assessments of AI's economic and social outcomes may depend heavily on choices over input and outcome measures, data availability, and what subpopulations contribute meaningfully to underlying data-generating processes.

This study makes a few key contributions. First, our approach allows us to characterize who the early-and, by extension, the most likely later-AI adopters are in the largest and most representative sample of firms to date. This approach is critical for getting the “denominator” right in estimating diffusion rates and identifying likely areas of impact. Prior work has estimated AI's potential using O*NET task descriptions (Brynjolfsson et al., 2018; Eloundou et al., 2023; Felten et al., 2021), online job postings (Acemoglu et al., 2022; Alekseeva et al., 2021; Babina et al., 2024; Goldfarb et al., 2023), and patents (Miric et al., 2023; Webb, 2019). However, direct firm-level measures of actual AI use are rare, as are rich organizational “intangibles”-particularly at scale. Privately held, small, and young firms are also typically lacking, despite being essential to contextualizing the phenomenon in the overall economy. The measurement constraints producing such gaps are nontrivial (McElheran, 2018; Miric et al., 2023), yet not insurmountable, as we show here. This new survey may serve as a template for follow-on research across other country and research contexts.⁴

Second, tying AI use to owner characteristics and motivations in a large sample of young firms adds to the nascent literature on entrepreneurial motivation (Cassar & Meier, 2018; Ganguli et al., 2021; Gans et al., 2019; Guzman et al., 2020). We document novel linkages between startup leadership, high-growth entrepreneurship, and adoption of frontier technologies, highlighting how difficult-to-observe backgrounds and motivations of founders predict early use of AI in production.

Third, our findings contribute updated and expanded insights to an important literature on drivers of information technology (IT) adoption, including organizational complements to IT use (Bloom et al., 2012; Bresnahan et al., 2002; Ichniowski et al., 1997), and recent emphasis on innovation and business strategy as complements to data and analytics (Brynjolfsson, Jin, et al., 2021; Wu et al., 2020). Identifying the correlates of AI adoption is an essential step in this agenda.

Finally, this study speaks to a literature on the geography of innovation and technology diffusion, dating back to Griliches (1957) that has gained momentum with the rise of digital technologies (Bloom et al., 2021; Forman et al., 2012; Kerr & Robert-Nicoud, 2020; Tambe, 2014).⁵ While certain familiar patterns of geographic concentration emerge with respect to AI, we find nuances in the relationship between urbanization and AI adoption. Moreover, we emphasize that employment-weighted geographic trends are indicative of AI's impact on workers, not solely on firms-a distinct perspective made possible by our comprehensive administrative data.

Our analysis shows that early AI use was low, skewed, and closely linked to the high-growth entrepreneurship essential to economic dynamism. However, its prevalence in the largest firms and key geographies raises concern about the sustainability of past dynamics. Our findings establish an early baseline for the use of AI in production. They also surface a number of novel insights into the industrial, technological, and organizational context of AI use to inform how we navigate AI's pitfalls and potential, moving forward.

[Page 4]
# 2 | MOTIVATION AND PRIOR WORK

Our framework for exploring the prevalence and implications of AI use builds on Zolas et al. (2020), which reported on the use of advanced business technologies, more broadly. Here, we focus specifically on AI and the technological and organizational context surrounding its use.

## 2.1 | Technology diffusion and its implications

A longstanding literature seeks to understand patterns of technology diffusion (e.g., Griliches, 1957), in large part due to the well-established relationship between technology use and firm productivity (Brynjolfsson & Hitt, 1996), as well as the role of GPTs in innovation and economic progress, more broadly (Bresnahan & Trajtenberg, 1995). Recent digital advances are gaining attention, including “big data," analytics, and data-driven decision making (Brynjolfsson, Jin, et al., 2021; Brynjolfsson & McElheran, 2016, 2019; Tambe, 2014; Wu et al., 2019). Yet, the speed of technological change raises questions about the applicability of prior intuitions to AI (e.g., Agrawal et al., 2019).

Recent research into AI's potential impacts has relied on O*NET task descriptions (Brynjolfsson et al., 2018; Eloundou et al., 2023; Felten et al., 2021), online job descriptions (Acemoglu et al., 2022; Alekseeva et al., 2021; Babina et al., 2024; Goldfarb et al., 2023), or combining the latter with patents and/or research publications (Bessen et al., 2021; Webb, 2019). Direct firm-level measures of AI use are rare, with exceptions in Europe, where samples are smaller (e.g., Czarnitzki et al., 2023; Hoffreumon et al., 2023). Studies of AI in other countries, such as Canada and China, have had to rely on yet different measurement approaches (Alexopoulos & Cohen, 2018; Beraja et al., 2023). Privately held, small, and young firms-essential to contextualizing the phenomenon in many economies and capturing dynamics are often unobserved, as are their organizational details. Our study contributes large-scale data, visibility to the intensity of AI use in production, representation and coverage of the diversity of US firms, and insights into the industrial, technological and organizational contexts (particularly for startups-see below) surrounding AI use.

Earlier IT diffusion research established the importance of commonly observed firm characteristics, such as industry, size, and location (Forman et al., 2005). We characterize AI use along these familiar dimensions, while disentangling often-confounded ones, such as age and technological sophistication. For the latter, we focus on data availability and cloud use, motivated by recent attention to "enabling" technologies (Gambardella et al., 2021; Kapoor & Teece, 2021), including findings linking data, cloud computing, and AI together (Bessen et al., 2022; Goldfarb et al., 2023; Lu et al., 2023). Studying AI in isolation from these other far-reaching innovations could obscure important interdependencies shaping its diffusion and potential impact (e.g., Rosenberg, 1963).

Similarly, while AI and robotics are frequently discussed together as automation technologies primed to transform the global workforce (Raj & Seamans, 2019), they are nevertheless typically studied in isolation. Robots primarily automate physical tasks (Dixon et al., 2021), whereas AI automates cognitive ones (Agrawal et al., 2019). Yet robotics is poised to increasingly rely on AI for greater autonomy and reprogrammability. Understanding their co-occurrence may be key to understanding how AI is mobilized in production activities, with attendant firm and labor market outcomes.

## 2.2 | Entrepreneurship and technology use

A key advantage of our research setting is detailed organizational data for a large sample of nonpublic, primarily young and small firms. Younger firms, in particular, are often missing from standard data sets, despite being vital to economic dynamism and innovation (Acemoglu et al., 2018; Decker et al., 2017; Guzman & Stern, 2020; Haltiwanger et al., 2013; Spulber, 2011a). We examine AI use among startups in detail, focusing first on characteristics that are largely fixed at founding and, as we establish empirically, associated with revenue growth early in the firm life cycle. Our overarching motivation for exploring the relationships to follow is that, if early AI use is concentrated among high-potential firms, we might expect greater economic and social impacts of AI as these firms scale. Conversely, if AI-related economic gains remain elusive (Brynjolfsson, Rock, et al., 2021), our findings may point to key frictions or measurement challenges for future study. Finally, if we can identify a relationship between AI use and later firm growth, this may indicate where causal links between AI use and firm performance will ultimately be found.

[Page 5]
### 2.2.1 | Owner characteristics: Education, experience, and age

We build on a growing body of evidence that certain early organizational markers can indicate a firm's growth potential and reliance on innovation in its strategy (e.g., Botelho et al., 2021; Guzman & Stern, 2020) by examining the extent to which this holds for its technology strategy. To begin, high-growth entrepreneurship has been linked to a number of founder characteristics and motivations (Guzman et al., 2020; Levine & Rubinstein, 2018) that might influence AI adoption. Intuitively, founders with advanced degrees are likely to lead firms that are more technology-focused or managed using a more-advanced technology. Experience (Nanda and Sørensen, 2010) and serial entrepreneurship (Lafontaine & Shaw, 2016) may also be correlated with better exploitation of technology-based business opportunities or adaptability to new technologies, in general.

With respect to age, Azoulay et al. (2020) find the mean founder age for fast-growing new ventures to be 45—older than is commonly understood. Yet it is consistent with tradeoffs between “vintage-specific human capital” (Chari & Hopenhayn, 1991) and intangible skills that take time to accumulate. When the latter complements digitization, this tradeoff is observed to create the best “fit” for midcareer workers compared with both older and younger employees (Barth et al., 2023). However, prior work has not explored how this nets out in the context of AI, whose newness may preference familiarity with the most-recent technology, particularly at the top of the organization.

### 2.2.2 | Founder motivation

Next, we expect that aspirations of entrepreneurs will shape the rate and direction of AI's impact. The smaller older firms that lag in advanced technology use (Zolas et al., 2020) may have been founded to pursue objectives other than growth, lacking the use cases, complementary inputs, and scale to justify AI adoption. The literature has delineated “lifestyle” from “high-growth” entrepreneurship (Hurst & Pugsley, 2011). We anticipate that lifestyle-focused owners— prevalent in American entrepreneurship—will be less likely to make the technology and organizational investments required to deploy AI in production.

Recent work also distinguishes between founders motivated by prosocial aspirations or workplace values and those motivated primarily by earning potential (Cassar & Meier, 2018; Ganguli et al., 2021; Guzman et al., 2020; Shah et al., 2019). While we cannot observe specific applications of AI, we expect founder motivation may foreshadow the potential for ethical or prosocial applications, versus ones with more-adverse consequences (Cowgill & Tucker, 2020) and thus include them in our characterization of AI's leading edge.

### 2.2.3 | Startup financing

Firm trajectories have further been linked to aspects of startup financing. Selection by—and synergies between—VCs and entrepreneurs have been linked to later growth.¹ We explore the relationship between VC funding, high-growth entrepreneurship, and AI use, which may arise for a variety of reasons. One channel could be selection: VCs may be able to better identify startups capable of developing or leveraging new AI technologies. Another could be treatment: the type of products and processes venture capitalists encourage may rely more significantly on AI use.

Higher initial capitalization may also reflect private information about firm growth potential. We thus also separately explore its relationship to AI use. Care is required, however, as capital intensity, even within narrowly defined industries, may reflect production strategy (McElheran et al., 2019) as much as firm “quality,” and is positively associated with the presence of other advanced technologies in manufacturing plants (Dinlersoz & Wolf, 2018). We thus leverage direct insights into dimensions of innovation and business strategy (rarely observed at scale) to help disentangle the source and level of financing from growth or “quality” as factors in AI adoption.

## 2.3 | Startup innovation and business strategies

Many of the organizational factors discussed above are relatively fixed early in the firm life cycle. However, we are also interested in the relationship between AI use and startups' innovation and business strategies, recognizing that they may be codetermined. A large and influential literature explores complementarities between organizational features

[Page 6]
and technology use (e.g., Aral et al., 2012; Bloom et al., 2012; Brynjolfsson & Hitt, 2000; Ichniowski et al., 1997). This literature, which focuses predominantly on large incumbents (e.g., Bresnahan et al., 2002) typically argues that organizational characteristics should be considered quasi-fixed in comparison to IT investment (e.g., Tambe et al., 2012), and takes as a key test of complementarity' the organization-technology correlations of the type we explore, here, with respect to AI.

Within this large and growing research area, the notion that commitments to certain innovation and business strategies (Ghemawat, 1991) might promote or complement technology use (rather than vice versa) has received scant attention. Concerning innovation, process versus product innovation is an important distinction—indeed, a tension— in firm dynamics and innovation strategy research (Cohen & Klepper, 1996). Whether and how this distinction matters with respect to frontier IT use, however, is less clear. On the one hand, less-“formal” process innovation may be critical for successful adoption of any new technology (Bresnahan & Greenstein, 1996; Feigenbaum & Gross, 2021; McElheran, 2015). On the other hand, formal IP protection may signal commitments to innovation and future growth (Dinlersoz et al., 2021, 2023; Guzman & Stern, 2020) that promote both AI use and economic impact. Understanding nuances in this relationship may be essential to unpacking adoption and growth dynamics related to ΑΙ.

Finally, recent work indicates that dimensions of a firm's business strategy will shape both the application and performance of new technologies (Brynjolfsson, Jin, et al., 2021; Li, 2023; McElheran & Jin, 2020; Wu et al., 2020). We extend this line of inquiry to understand AI use among startups with different business strategies, focusing on the distinction between growth-oriented strategies versus others, such as a low-cost or "niche" positioning (e.g., Porter, 1980).

## 2.4 | Geography of startups

Research into both technology diffusion and entrepreneurship has long emphasized the importance of geography for understanding patterns of technology use, location choice, and economic outcomes (e.g., Delgado et al., 2010; Forman et al., 2012, 2016). Recent work has pointed to growing concentration, both of frontier technologies (Tambe, 2014) and of startup activity (Guzman, 2023). VC- and innovation-related spillovers may further contribute to the emergence of hubs for startups leveraging specific technologies (Jaffe et al., 1993; Kerr & Robert-Nicoud, 2020; Samila & Sorenson, 2011). While AI is still in a relatively early stage of its geographic diffusion, “pioneering” tech locations have been found to retain a considerable share of the relevant employment (Bloom et al., 2021), and distance from "hotspots" of AI invention has slowed its adoption for certain firms (Bessen et al., 2021). Thus, Al's future path will likely depend on its early geographic dispersion. We do not seek to pin down specific drivers, focusing instead on describing the dispersion of AI use in production and its implications for workers, broadly defined. That said, shedding light on key geographic patterns of AI adoption is a key objective of our analysis.

# 3 | DATA AND NEW DESCRIPTIVE “FACTS"

This study provides the first in-depth look at AI adoption from the ABS. Introduced in 2018, the ABS consolidates three prior surveys of US firms. New designed-for-purpose questions on technology use were added to existing questions that provide, for relevant firms, ownership and owner characteristics, startup financing, IP use, and other details of innovation and business strategy.² We sketch out the data construction and novel descriptive statistics here, beginning with our baseline sample. See Data Appendix B for details.

## 3.1 | Baseline sample

The 2018 ABS was sent to 850,000 firms nationwide. Approximately 583,000 firms responded to the survey, 573,000 of which were linked to the LBD. The LBD is curated by Census to provide a comprehensive panel of microdata on employment, revenue, and payroll for the private nonfarm economy (Chow et al., 2021). The LBD tracks firms from their birth as an employer to death, accounting for mergers and acquisitions. This provides the basis for our systematic exploration of early- and later-stage growth patterns for firms in the ABS.

[Page 7]
Leveraging the LBD mitigates concerns that we could overlook dynamic entrepreneurial firms, which are often excluded from standard data sets comprised of larger incumbents (e.g., Compustat). Conversely, it ensures we do not omit older firms that might be systematically excluded if sampling depended on the presence of advanced technology (such as participating on a digital platform). We call this sample of 573,000 firms the ABS-LBD linked sample (column 1, Table 1).

For most of our analyses, we restrict attention to the 447,000 firms for which we have sufficiently complete information on AI use. Descriptions of average firm size and age for this baseline sample are presented in column (2) of Table 1. We weight the firms in our samples to better represent the firm size, age, and industry distributions of the population of employer businesses in the US-wide Business Dynamics Statistics (BDS). The vast majority of US firms are very small,¹⁰ which is reflected in our baseline sample. The average firm in this sample has roughly 62 employees, but only 21 when weighted. Average age is around 16 years (regardless of weighting). Weighting makes our sample representative of over 4 million firms across the US economy (column 2, Table 1).

Investigating the organizational context, linkages to revenue growth, and geography of AI use impose other sample restrictions. These vary by analysis and are discussed as they arise, below.

## 3.2 | New measures for the digital age: Digitization, cloud computing, and advanced business technologies

The technology module of the 2018 ABS contains three new and connected questions on digitization and technology use. The first queries firms' reliance on data, widely regarded as a key input to more advanced uses of digital technologies (Brynjolfsson & McElheran, 2016, 2019). Over 65% of the ABS–LBD linked sample reported having at least one type of information in digital format.

A second enabler is computing power to store and analyze massive quantities of data. Thus, the second question probes the extent to which firms rely on cloud services, which have shifted the cost structure and speed of access to IT for many US firms (Goldfarb et al., 2023; Jin & McElheran, 2017). Around 43% of firms in our sample purchased cloud services for at least one IT function.

The third question, and primary focus of this paper, asks about the use of various advanced business technologies in producing goods or services, including intensity of use. Defined in Table 2, these include five commonly associated

**TABLE 1** Summary statistics of firm size and age by sample.

| | (1) ABS-LBD linked sample | (2) Baseline sample | (3) Owner and revenue sample | (4) Startup sample | (5) Startup sample in specific industries |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Employment (unweighted)** | 89.32 | 61.69 | 17.68 | 10.39 | 9.11 |
| **Employment (weighted)** | 26.28 | 20.77 | 9.78 | 7.4 | 6.91 |
| **Age (unweighted)** | 16.33 | 16.60 | 8.94 | 2.87 | 2.87 |
| **Age (weighted)** | 15.61 | 15.94 | 8.66 | 2.82 | 2.83 |
| **Observations (unweighted)** | 573,000 | 447,000 | 209,000 | 75,000 | 28,000 |
| **Observations (weighted)** | 5,180,000 | 4,050,000 | 1,970,000 | 740,000 | 228,000 |

*Notes*: Tabulations based on 2018 ABS data linked with the 2017 Longitudinal Business Database (LBD) data for size and age. Firms that did not respond to any of the 2018 ABS survey are excluded. See Zolas et al. (2020) for further details and breakdown of the size and age distribution for the full sample of linked ABS-LBD firms. Weights are computed by stratifying the firms in the 2017 LBD and our final sample of firms in the ABS on firm size, age, and industry. These strata are defined by the 19 two-digit NAICS sectors and the 12 firm size and 12 firm age groups used in the BDS. Samples in columns (2)–(4) are restricted by needing to contain information on the primary owner and are born on or after 1997, the first year that the LBD contains firm-level revenue measures. “Startups” are defined as being born on or after 2012. Specific Industries refers to a subset of two-digit NAICS sectors that are more engaged in AI usage: Manufacturing (“31–33”), Information (“51”), Professional and Scientific Services (“54”), and Healthcare (“62”).

*Abbreviations*: ABS, Annual Business Survey; BDS, Business Dynamics Statistics; NAICS, North American Industry Classification System.

[Page 8]
382
-WILEY-
Journal of Economics &
Management Strategy
MCELHERAN ET AL.

TABLE 2 Definitions of technologies.

| | |
|---|---|
| Augmented reality | Technology that provides a view of a real-world environment with computer-generated overlays. |
| **Automated-guided vehicles (AGV) or AGV systems** | A computer-controlled transport vehicle that operates without a human driver. AGVs navigate facilities through the use of software and sensors. |
| Automated storage and retrieval systems | Technology that locates, retrieves, and replaces items from predetermined storage locations. |
| **Machine learning** | Computer algorithms that use data to improve their predictive performance without being reprogrammed. |
| **Machine vision** | Technology used to provide image-based automatic inspection, recognition or analysis. |
| **Natural language processing** | Technology that allows a computer to process human speech or text. |
| Radio-frequency identification system | A system of tags and readers used for identification and tracking. Tags store information and transmit them using radio waves. Readers maybe mobile or fixed in place. |
| Robotics | Reprogrammable machines capable of automatically carrying out a complex set of actions. |
| Touchscreens/kiosks for customer interface (examples: self-checkout, self-check-in, touchscreen ordering) | A computer with a touchscreen that allows a customer to receive information or perform tasks related to the business, such as registering for a service or purchasing items. |
| **Voice recognition software** | Software that converts speech to text or executes simple commands based on a limited vocabulary or executes more complex commands when combined with natural language processing. |

*Notes:* "AI-related" technologies for the purposes of this study are in bold. Definitions validated during cognitive testing of the survey instrument. See Zolas et al. (2020) for further details.
*Abbreviation:* AI, artificial intelligence.

with AI (bolded): machine learning, machine vision, natural language processing, voice recognition software, and automated-guided vehicles (AGVs).¹¹ Tabulated responses to these five items, conditional on some use of the specified technology, are reported in Figure 1. It is useful to keep in mind that only 2% of the firms in the overall unweighted ABS–LBD linked sample reported any use of AI.¹² Thus, the y-axis here represents the number (not share) of firms. Note the considerable dispersion across both specific technologies and intensities of use. To our knowledge, this is the first study to capture such variation in firm-level AI use.

Also reported in Figure 1, adoption rates of specific AI-related technologies were below 3%, across the board— ranging from a high of 2.9% in the case of machine learning, to a low of 0.8% for AGVs. Testing of each technology— presumably a leading indicator of use in production—was even lower (less than 1% each), suggesting that these levels were not poised to change dramatically in the wake of our study.

## 3.3 | Early AI use: Low and skewed

For our main analyses, we collapse different technologies and intensities of use into a single binary indicator of *any use* of AI in production According to this definition, the share of firms in the baseline sample using AI as of 2017 was 5.8%. The share testing at least one AI-related technology (but not yet using it in production) was 1.1% (see Figure 1).

This level of AI diffusion is significantly lower than that reported elsewhere, for example, in the European Commission survey of AI (Kazakova et al., 2020) or other private surveys by McKinsey (Chui & Malhotra, 2018), Deloitte (2018), or PwC (2019). However, these surveys do not claim to be representative, oversampling larger, often publicly traded companies. In contrast, our baseline sample includes many small firms for which AI adoption is quite limited—yet whose inclusion allows us to estimate the correct denominator for country-wide AI usage rates.

[Page 9]
MCELHERAN ET AL.
383
Journal of Economics & Management Strategy
WILEY

[CHART: A bar chart titled "FIGURE 1 Prevalence of AI-related business technologies (AI) in the United States by 2017." The chart displays data for five categories on the x-axis: Automated Vehicles, Machine Learning, Machine Vision, Natural Language, and Voice Recognition. The y-axis represents a count from 0 to 7,000. Each category has four bars, color-coded according to the legend: "Testing but not using" (purple), "Less than 5%" (green), "Between 5% and 25%" (orange), and "More than 25%" (dark red). Data labels are present above some bars. For Automated Vehicles: 0.8% (2.5%) and 0.2% (1.2%). For Machine Learning: 2.9% (8.5%) and 0.9% (4.3%). For Machine Vision: 1.8% (5.1%) and 0.4% (2.1%). For Natural Language: 1.3% (5.6%) and 0.5% (2.3%). For Voice Recognition: 2.5% (9.6%) and 0.2% (3.0%). Below the x-axis, there are summary statistics: "Any Use - 5.8% (18.2%)" and "Any Test - 1.1% (2.0%)".]

FIGURE 1 Prevalence of AI-related business technologies (AI) in the United States by 2017. Notes: Tabulations (bars) based on unweighted and nonimputed responses from the full ABS-LBD linked sample. “Don't Know” and missing responses are excluded from this figure. The figures listed above the bars reflect the firm-weighted usage rates, followed by employment-weighted usage rates in parentheses (both nonimputed and from our baseline sample). The figures in red font indicate the “Testing” rate for each technology. “Use” is defined as having responded with “In use for less than 5% of production or service,” “In use for between 5%–25% of production or service,” or “In use for more than 25% of production or service” in the “Business Technologies” module of the ABS. Shares are computed using the LBD tabulation weights of firm counts divided by the total number of firms (excluding those that responded with “Don't Know” or missing). Employment weights are calculated by multiplying the LBD tabulation weights by firm employment. Abbreviations: ABS, Annual Business Survey; AI, artificial intelligence; LBD, Longitudinal Business Database. [Color figure can be viewed at wileyonlinelibrary.com]

While these low average rates are informative—and useful for counteracting potentially excessive “exuberance” related to AI—they paint an incomplete and potentially understated picture of AI use in America. As for many advanced business technologies (e.g., Zolas et al., 2020), early AI use appears highly skewed and concentrated among larger firms. Figure 2a reports AI use by firm size for different intensities.¹³ Note that the majority of firms with more than 5,000 employees reported at least some use of AI. Over a quarter of the largest firms reported using AI intensively.

This skewness in both AI presence and intensity underscores the potential impact of AI not only on firms, but also on employees at these firms. Returning to Figure 1, employment weighting (in parentheses) indicates machine learning prevalence closer to 8.5%, and employment-weighted usage of any AI technology of roughly 18.2%.

## 3.4 | Who adopts AI: Firm industry, size, and age

Our rich administrative data grants insights into key characteristics of early AI users—the *who* of interest in this study. Figure 2b reports AI use and intensity by sector. Manufacturing and information-sector firms led in early AI adoption, each with roughly 12% extensive-margin adoption rates. Both also led in intensity of use, with health-related firms close behind. Lagging sectors included construction and retail trade, at roughly 4%, each. Finance, insurance, and real estate (“FIRE”) sectors had adoption rates below 6% with limited intensity, despite ranking highly in digitization of information—see, for example, fig. 2 in Zolas et al. (2020).

Table 3 zooms in on the nonmanufacturing industries (at the four-digit NAICS level) where AI was most prevalent. On a firm-weighted basis, medical and diagnostic laboratories had an uptake above 23%. Other high-AI industries tended to be high tech, such as software publishing (nearly 16%) and computer systems design (14%), though with exceptions, such as physicians' offices (19%). Data processing and related services, which includes cloud services, reported AI use around 14%. This is notable, as many of these services represent industries where we expect development of applications of AI for use in other sectors of the economy (e.g., Bresnahan, 2023).

[Page 10]
[CHART: A horizontal stacked bar chart titled '(a)' showing AI use intensity and testing rates by firm size. The y-axis lists firm sizes in terms of employees, from '1-4 Employees' at the bottom to '10,000+ Employees' at the top. The x-axis represents the percentage from 0% to 70%. The bars are stacked to show 'Testing', 'Low Intensity', 'Medium Intensity', and 'High Intensity' usage. The legend indicates these four categories. Generally, larger firms show a higher percentage of AI use across all intensity levels.]

[CHART: A horizontal stacked bar chart titled '(b)' showing AI use intensity by sector. The y-axis lists various sectors like 'Agriculture,..., Mining, Utilities', 'Construction', 'Manufacturing', etc. The x-axis represents the percentage from 0% to 14%. The bars are stacked to show 'Low Intensity', 'Medium Intensity', and 'High Intensity' usage. The legend indicates these three categories. The 'Information' sector shows the highest intensity of use.]

FIGURE 2 AI uses intensity and testing rates (a) by firm size and (b) by sector. Notes: These figures visually represent the weighted share of firms that indicate the intensity of use of at least one of the following business technologies: automated-guided vehicles, Machine Learning, Machine Vision, Natural Language Processing, or Voice Recognition (see Table 2). Values are based on the imputed probabilities for respondents who answered "Missing" or "Don't Know" to one or more of the aforementioned business technologies. High intensity corresponds to respondents utilizing at least one of the AI-based business technologies "In use for more than 25% of production or service." Medium intensity corresponds to "In use for between 5%-25% of production or service." Low intensity corresponds to "In use for less than 5% of production or service." AI, artificial intelligence. [Color figure can be viewed at wileyonlinelibrary.com]

We control for this significant industry-based heterogeneity at the six-digit NAICS level (a degree of granularity difficult to achieve in standard data sets)¹⁴ to highlight other patterns of interest. Table 4 reports the likelihood of using AI by size and age, including state-by-industry controls. Conditional correlations show AI usage increasing monotonically with size. In column (1), firms in the top percentile of their industry's employment distribution were nearly nine percentage points (pp) more likely to use AI compared to below-median firms. In contrast, we find AI presence decreasing almost monotonically with age, though magnitudes are smaller. The oldest firms were 1-2 pp less likely to use AI than firms younger than their industry's median age.¹⁵

[Page 11]
MCELHERAN ET AL.
385

Journal of Economics & Management Strategy
WILEY

**TABLE 3** Top nonmanufacturing industries (four-digit NAICS) for AI use.

| NAICS | NAICS description | |
| :--- | :--- | :--- |
| | **Mean (all industries)** | **0.058** |
| 6215 | Medical and diagnostic laboratories | 0.237 |
| 6211 | Offices of physicians | 0.190 |
| 5112 | Software publishers | 0.156 |
| 5415 | Computer systems design and related services | 0.141 |
| 5182 | Data processing, hosting, and related services | 0.139 |
| 5191 | Other information services | 0.126 |
| 6214 | Outpatient care centers | 0.121 |
| 5411 | Legal services | 0.120 |
| 1151 | Support activities for crop production | 0.119 |
| 4248 | Beer, wine, and distilled alcoholic beverage merchant wholesalers | 0.112 |

*Notes*: Tabulated from the ABS-LBD linked sample (column 1, Table 1). Shares computed using the LBD tabulation weights of firm counts, divided by the total number of firms (including those that responded with "Don't Know" or missing), then scaled up by the total number of nonmissing and "Don't Know" responses for each technology. The 2017 industry figures from the LBD are the figures listed in the tables. Industry tabulations for multiunit firms are generated from the largest payroll industry within the firm (if there is a tie, then the industry with the most employment is used).

*Abbreviations*: ABS, Annual Business Survey; AI, artificial intelligence; LBD, Longitudinal Business Database; NAICS, North American Industry Classification System.

## 3.5 | What gets Adopted: Technology details and interdependencies

Column (2) of Table 4 sheds new light on what technologies get adopted, adding indicators for digitization and cloud computing. Controlling for the above observables, digitization is predictive of AI use: firms that reported having at least one type of information in digital format were 2 pp more likely to report some AI use. Firms that reported purchasing cloud services for at least one IT function were 5 pp more likely to use AI. Further, these margins of technology use appear interconnected, per Figure 3, which shows a Sankey Diagram of firms that used one or more of each type of technology. Among firms that reported early AI use, reliance on cloud computing was prevalent, while cloud computing use, in turn, was highly correlated with digitization. Given this apparent technological hierarchy, it is unsurprising that we further find more-intensive reliance on data and cloud better predicted AI adoption (see Figure A4), consistent with accumulating digital capabilities (e.g., Tambe et al., 2020) that enable frontier technology adoption.

We further observe variation by industry in terms of what specific AI-related technology (among those in Table 2) was most prevalent. Reported in Table A1, while more-generic machine learning was highly prevalent in computer systems and data processing industries, industries not always considered “high tech" led in the use of specific technologies. For example, AGVs, while used by fewer than 1% of firms nationwide, were present at roughly nine times that rate in support activities for crop production in the agriculture sector. Similarly, machine vision was most prevalent in technical and trade schools in the education sector (nearly 5%), while voice recognition was most prevalent in healthcare settings and legal services.

This industry-based heterogeneity also hints at complementarities between AI and other labor-saving technologies, such as robotics. Robotics adoption based on ABS responses (1.3% of the ABS-LBD linked sample) was significantly lower than that for AI. However, the overlap with AI appears fairly significant, with the majority of robotics adopters (57.5%) reporting using at least one AI technology. Figure 4 provides a sectoral breakdown of the overlap of firms that use AI, robotics, or both, with the greatest overlap in the manufacturing, wholesale, and education sectors.16

## 3.6 | Al in entrepreneurship: Owner characteristics, startup conditions, and firm strategies in AI-using startups

The ABS further contains, for a large subsample, detailed information on the owners of the firm, their reasons for owning the business, financing at startup or acquisition, IP strategy, and related innovation and business strategies.17 Given the economic importance of young firms, we leverage this unusual visibility to the organizational context to

[Page 12]
**TABLE 4 Correlates of AI use—Firm size, age, and other technology use.**

| Description | (1) Use AI | (2) Use AI |
| :--- | :--- | :--- |
| Employment percentile 51–75 | 0.011*** | 0.004*** |
| | (0.001) | (0.001) |
| Employment percentile 76–90 | 0.025*** | 0.012*** |
| | (0.001) | (0.001) |
| Employment percentile 91–95 | 0.036*** | 0.019*** |
| | (0.002) | (0.002) |
| Employment percentile 96–99 | 0.053*** | 0.032*** |
| | (0.002) | (0.002) |
| Employment percentile 99+ | 0.086*** | 0.063*** |
| | (0.004) | (0.004) |
| Age percentile 51–75 | −0.006*** | −0.001 |
| | (0.001) | (0.001) |
| Age percentile 76–90 | −0.011*** | −0.004*** |
| | (0.001) | (0.001) |
| Age percentile 91–95 | −0.015*** | −0.006*** |
| | (0.002) | (0.002) |
| Age percentile 96–99 | −0.022*** | −0.013*** |
| | (0.003) | (0.003) |
| Age percentile 99+ | −0.008*** | −0.001 |
| | (0.002) | (0.002) |
| Use: Digitization | | 0.019*** |
| | | (0.001) |
| Use: Cloud | | 0.050*** |
| | | (0.001) |
| State-by-industry controls | Yes | Yes |
| Observations (rounded) | 447,000 | 447,000 |
| R² | 0.102 | 0.115 |

Notes: Standard errors in parentheses. The coefficient estimates represent the relative AI usage rates across size and age percentiles within a six-digit (NAICS) industry, by state (State-by-industry controls). The underlying sample is the baseline sample (column 2, Table 1).
Abbreviations: AI, artificial intelligence; NAICS, North American Industry Classification System.
*, **, and *** denote significance at 10%, 5%, and 1%, respectively.

delve more deeply into roughly 75,000 startups (0–5 years old as of 2017). Firms in this “startup sample” (column 4, Table 1) are just under 3 years old, on average, with around 10 employees and representatives on a firm-weighted basis of 740,000 firms. We next describe these detailed measures and report unconditional means, both across this sample as well as by whether or not the firm used AI, in Table 5.

### 3.6.1 | Owner education, experience, age, and aspirations

The ABS asks roughly 20 questions about up to four business owners; we focus on the primary owner (based on ownership share) in Panel A of Table 5. See survey details in Data Appendix B.

[Page 13]
MCELHERAN ET AL.
<br>
Journal of Economics & Management Strategy
WILEY-
387

**FIGURE 3** Technology interdependencies. Notes: Sankey representation of firm counts in the ABS-LBD linked sample (column 1, Table 1) as they progress from no technology adoption to reliance on digital information, then cloud computing, and finally AI adoption. The size of the gray area is representative of the number of firm progressing to the next "stage" of technology use. Note that the calculations are made using imputed values for missing responses. Use of AI constitutes the weighted count of firms that indicate use of at least one of the following business technologies: Automated-Guided Vehicles, Machine Learning, Machine Vision, Natural Language Processing, and Voice Recognition (Table 2). ABS, Annual Business Survey; AI, artificial intelligence; LBD, Longitudinal Business Database. [Color figure can be viewed at wileyonlinelibrary.com]

[CHART: A Sankey diagram illustrating technology adoption pathways. A single large flow labeled "ABS Sample" on the left splits into four subsequent stages. The first split is into "Digitization" and "None". The "Digitization" flow then splits into "Cloud Computing" and a smaller flow that goes to "None". The "Cloud Computing" flow then splits into "AI Adoption" and a smaller flow that goes to "None". The "None" category accumulates flows from each stage, representing firms that do not adopt the next technology.]

[CHART: A horizontal stacked bar chart titled "AI and robotics use by sector". The y-axis lists various industry sectors: Agriculture,..., Mining, Utilities; Construction; Manufacturing; Wholesale Trade; Retail Trade; Transportation & Warehousing; Information; Finance, Insurance, Real Estate; Professional Services; Management & Administrative; Education; Health Care; Other (Arts, Food, Other). The x-axis represents percentages from 0% to 100%. Each bar is divided into three segments representing "AI Only" (dark gray), "AI & Robotics" (medium gray), and "Robotics Only" (light gray). For example, the "Information" sector shows the highest proportion of "AI Only" use, exceeding 90%. "Manufacturing" shows a significant portion of all three categories, with a notable "Robotics Only" segment. The legend at the bottom clarifies the color coding: ■ AI Only ■ AI & Robotics ■ Robotics Only.]

**FIGURE 4** AI and robotics use by sector. Notes: Percentage of firms that use AI or robotics among firms in the ABS-LBD linked sample that also reported using either an AI-based technology or robotics (roughly 34,000 firms). AI use is defined by the weighted share of firms by sector that indicates the use of at least one of the following business technologies: Automated-Guided Vehicles, Machine Learning, Machine Vision, Natural Language Processing, and Voice Recognition. Robotics use is collected from the same survey question (see Table 2) and similarly weighted. ABS, Annual Business Survey; AI, artificial intelligence; LBD, Longitudinal Business Database. [Color figure can be viewed at wileyonlinelibrary.com]

Starting with education, while 22.4% of all primary owners in our startup sample reported holding an advanced degree (master's, doctoral, or professional-see column 1), this rises to 31.5% among AI users (column 2). Owners of AI-using startups were relatively more likely to have owned a prior business (43.8%) compared with those without AI (41.2%) in column (3). Owners of AI-using startups also tended to be slightly younger, as well.¹⁸

Panel B in Table 5 describes the "very important" reasons that owners (primarily founders) may report for owning the business. The biggest differences between AI-using startups and the rest (column 4) were “Help and/or become more involved in my community" (6.6 pp difference) and "Best avenue for my ideas/goods/services" (5.1 pp difference). Other reasons are tabulated for completeness in Table 5; however, a binary indicator of lifestyle-focused (“Flexible hours" or "Balance work and family") versus other motivations turns out to be the most tractable and intuitive approach in a richly specified regression framework (see below), even though the unconditional means are not strikingly different at 0.8 pp.

[Page 14]
TABLE 5 Firm characteristics by AI use status (%) startup sample.

| | (1) Full sample | (2) Use AI | (3) Do not use AI | (4) Difference |
| :--- | :--- | :--- | :--- | :--- |
| **A. Primary owner characteristics** | | | | |
| Hold advanced degree | 22.4 | 31.5 | 21.9 | 9.6 |
| Owned prior business | 41.4 | 43.8 | 41.2 | 2.6 |
| Missing age | 7.4 | 9.4 | 7.2 | 2.2 |
| Owner age (0-34) | 11.5 | 11.2 | 11.5 | -0.3 |
| Owner age (35-54) | 54.5 | 55.1 | 54.5 | 0.6 |
| Owner age (55+) | 26.6 | 24.7 | 26.8 | -2.1 |
| **"Very Important" reasons for owning the business** | | | | |
| Wanted to be own boSS | 63.9 | 62.9 | 64 | -1.1 |
| Flexible hours | 54.5 | 52.8 | 54.7 | -1.9 |
| Balance work and family | 56.4 | 55.1 | 56.4 | -1.3 |
| Opportunity for greater income | 63.0 | 62.9 | 63 | -0.1 |
| Best avenue for ideas/goods/services | 56.9 | 61.8 | 56.7 | 5.1 |
| Unable to find employment | 7.2 | 9.0 | 7.1 | 1.9 |
| Working for someone else not appealing | 30.5 | 31.5 | 30.5 | 1.0 |
| Always wanted to start own business | 48.5 | 49.4 | 48.5 | 0.9 |
| Entrepreneurial role model | 24.5 | 27.0 | 24.3 | 2.7 |
| Carry on family business | 9.9 | 11.5 | 9.9 | 1.6 |
| Help or become involved in community | 24.1 | 30.3 | 23.7 | 6.6 |
| Other reasons | 8.0 | 10.6 | 7.8 | 2.8 |
| Lifestyle reason | 63.6 | 62.9 | 63.7 | -0.8 |
| **B. Startup financing** | | | | |
| Funded by VC | 0.9 | 2.9 | 0.8 | 2.1 |
| Missing startup capitalization | 8.4 | 6.3 | 8.5 | -2.2 |
| Startup capitalization <25K | 38.4 | 38.2 | 38.4 | -0.2 |
| Startup capitalization 25K-1M | 38.9 | 42.7 | 38.8 | 3.9 |
| Startup capitalization 1M+ | 2.5 | 3.8 | 2.4 | 1.4 |
| Don't know startup capitalization | 11.8 | 10.3 | 11.9 | -1.6 |
| **C. Innovation and business strategy** | | | | |
| Process innovation | 19.9 | 39.3 | 18.7 | 20.6 |
| Product innovation | 53.6 | 66.3 | 52.8 | 13.5 |
| Patents owned or pending | 2.1 | 5.2 | 1.9 | 3.3 |
| IP is very important | 19.5 | 40.4 | 18.1 | 22.3 |
| Growth-oriented innovation strategy | 69.5 | 77.5 | 68.9 | 8.6 |
| **D. Geography** | | | | |
| In micropolitan or rural CBSA (<50, 000) | 22.8 | 20.0 | 23.0 | -3.0 |
| In small-sized CBSA (<250, 000) | 9.1 | 8.1 | 9.1 | -1.0 |

[Page 15]
**TABLE 5** (Continued)

| | (1) <br> Full sample | (2) <br> Use AI | (3) <br> Do not use AI | (4) <br> Difference |
| :--- | :--- | :--- | :--- | :--- |
| In medium-sized CBSA (<1, 000, 000) | 17.8 | 17.1 | 17.8 | -0.7 |
| In large-sized CBSA (1, 000, 000+) | 50.3 | 55.1 | 49.9 | 5.2 |

*Notes*: "Use" is defined as having responded with "In use for less than 5% of production or service," "In use for between 5%-25% of production or service," or "In use for more than 25% of production or service" for the category listed on any of the AI-based Business Technologies. The "Growth-oriented innovation strategy" indicator is equal to 1 if a firm responded that a focus on introducing new goods or services, reaching new customer groups, or opening up new domestic or export markets was a "very important" innovation strategy for the business. The underlying sample is our startup sample (column 4, Table 1). Abbreviations: AI, artificial intelligence; CBSA, core-based statistical area; VC, venture capital.

### 3.6.2 | Startup financing

Next, we explore the source and size of capitalization at startup or acquisition in panel C of Table 5. For VC funding, which was uncommon across the sample, we observe a sizable difference in means: 2.9% of AI-using startups were funded by VC (column 2), compared with only 0.9% of all startups in the sample (column 1). AI-using startups also reported larger capitalization, on average. Combining rows in this panel, 46.5% reported startup capital of more than $25,000 compared with only 41.4% of all startups; 3.8% reached or exceeded $1 million, versus 2.4%, on average.

### 3.6.3 | Innovation and business strategies

The largest unconditional differences between AI-using and other startups centers on innovation and business strategies (column 4 of panel D, Table 5). Process and product innovation within the last 3 years (2015–2017) are separate ABS questions. The former, while reported by only 19.9% of startups, overall, was far more prevalent among AI users (39.3%). The latter was more common overall (53.6%) and more prevalent among AI users (66.3%). AI-using startups relied on formal IP at higher rates, as well. The prevalence of patents owned or pending among such firms was 5.2%, versus 2.1% overall. IP was reported to be “very important" at a rate of 40.4% among AI users, versus only 18.1% among those not using AI in production.

We collapse the 14 business strategies measured in the ABS (see Appendix B) into an indicator having a growth-oriented strategy, based on whether introducing new goods or services, reaching new customer groups, or opening up new domestic or export markets were “very important.” AI-using startups were growth-oriented at a rate of 77.5%, compared with 68.9% of non-AI users.

### 3.7 | Where: The geography of AI-using startups

The last set of descriptives in Table 5 speaks to the *where* of our study. In panel D, we take as our unit of aggregation CBSAs.19 While a sizeable share of startups in our sample (22.8%) are in very small CBSAs (fewer than 50,000 people), over 50% are in metro areas of 1 million or more, with 55.1% of AI-using startups located in a large CBSA.

We assess AI prevalence within each CBSA in two ways: first, as the share of single-unit startups that use AI; and, second, in terms of the share of employment among single-unit startups accounted for by AI-using firms.20 The ranking for the largest CBSAs is shown on a map in Figure 5.21 Bubble sizes represent the number of AI-using startups present in the CBSA, while the color gradient indicates the percentile rank of the CBSA in terms of the AI usage rate—lighter colors correspond to greater prevalence of AI use among young single-unit firms in that CBSA.

Some high-level patterns are apparent. Areas known for pioneering technologies, such as Silicon Valley in California and Research Triangle in North Carolina, 22 show high concentrations of AI use among startups, as shown by the lighter colors. 23 Yet hubs for AI use are apparent throughout the South and the West, as well. The share of startups using AI was high in the metro areas surrounding Nashville, San Antonio, Las Vegas, New Orleans, San Diego, and Tampa.

[Page 16]
390
-WILEY-
Journal of Economics &
Management Strategy
MCELHERAN ET AL.

[CHART: A map of the United States showing large core-based statistical areas (CBSAs). Each CBSA is represented by a circle. The size of the circle indicates the number of AI-using firms, and the color indicates the AI usage rate percentile. The legend shows a color gradient for "AI Percentile" from 0 (yellow) to 100 (dark purple). It also shows three sample circles for "AI Firms" corresponding to 10000, 20000, and 30000 firms.]

**FIGURE 5** AI use rates by single-unit startups across large core-based statistical areas (CBSAs). Notes: The map includes the largest (population >1,000,000) CBSAs. Bubble sizes in the map represent the (firm-weighted) number of single-unit startups (i.e., firm age ≤5 years) that use AI within each CBSA, and the color gradient represents the percentile rank of the usage rate of AI across single-unit startups within the largest CBSAs. Unlike our "startup sample" described in Table 1 (and used for regressions in Tables 6a, 6b, and 7), the underlying sample of this figure is not restricted to firms with owner or revenue information. Rather, the underlying sample is a subset of our baseline sample—specifically, single-unit startups located in large CBSAs (roughly 30,000 firms). AI, artificial intelligence. [Color figure can be viewed at wileyonlinelibrary.com]

The Northeast and Midwest display lower **AI intensity** as a share of the firm population (represented by darker colors). However, larger metro areas typically have more firms, in general. Thus, areas such as New York City, Los Angeles, Chicago, and Washington DC are prominent in terms of the number of AI-using startups, while within these areas AI usage is not particularly intense.²⁴

This view of AI geography shifts somewhat when we use employment-weighted adoption rates across CBSAs, as shown in Figure A2. This assessment, based on the share of employment among single-unit startups accounted for by AI-using firms, provides insight into worker exposure to AI. Worth noting, this approach is not based on firm demand for particular skills and assumes that the use of AI in production at the firm constitutes exposure of all of its employees to AI. Among US startups, Riverside in California actually supersedes the Bay Area on an employment-weighted basis (see Table A2). Additional locations become prominent using this approach, primarily in the Midwest and Mid-Atlantic, including Louisville, Columbus, Austin, and Atlanta. Locations in the South tend to fall, in a relative sense, as a result of employment weighting.²⁵

Table A2 provides a list of CBSAs, ordered alphabetically alongside their AI usage rate and ranking. Firm-weighted rankings (corresponding to Figure 5) are in column (1), while column (2) relies on employment weighting (Figure A2). The bottom panel summarizes overall shares for micropolitan, small-, and medium-sized CBSAs. While AI usage rates are generally lower in the smaller CBSA groups, they are not too far below the corresponding rates in the largest CBSAs. We return to the role of CBSA size in AI adoption in Section 4.3.

# 4 | REGRESSION ANALYSIS

## 4.1 | Methodology

Moving beyond novel descriptive statistics, our empirical approach assesses whether the organizational features described above may help predict patterns of AI adoption, as well as how the unconditional patterns might shift in a more richly specified regression framework. This will shed light on the relative importance of various drivers of AI use, as well as clarify the extent to which AI adoption is associated with early indicators of a young firm's economic potential.

To do this, we proceed in steps. First, we establish the extent to which these traits do indeed identify startups that turned out to be “high quality” in terms of having high growth early in life. For these analyses, we measure

[Page 17]
MCELHERAN ET AL.
<br>
Journal of Economics & Management Strategy &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&-WILEY 391

early-growth trajectories by taking the average of the annual log-difference revenue (r) growth rate over the first 3 years of a firm:

$g = \frac{1}{3} \sum_{t=1}^{3} \ln \left(\frac{r_{t}}{r_{t-1}}\right)$ (1)

After assessing which characteristics are associated with early growth, we fit a linear probability model using Ordinary Least Squares to explore the extent to which the same firm features may also predict AI use.
Beyond characterizing patterns of early AI use, we are interested in how its application may be related to firm performance. To explore this, we examine whether AI use had a significant association with firm growth after controlling for a rich set of observables. We extend this by further measuring average growth over the 3 years around the reference year of 2017 (2016–2018), again using (1). To understand this later-stage growth, we need to expand the sample to include all firms with the relevant owner and revenue data (column 3, Table 1), as startups are by definition in the early stages of their life cycle. This approach leverages the LBD more fully, while nevertheless introducing other sampling pressures, including potential survivor bias²⁶ and the exclusion of publicly traded and much-older firms (over 20 years old—see Appendix B).
Finally, our analysis does not aim to establish a causal relationship between firm characteristics and AI adoption or between adoption and growth. These findings will be most appropriately interpreted as suggestive of linkages between technology use and performance, with careful causal identification left as a challenge for future work.

## 4.2 | Markers of high-growth entrepreneurship

Table 6a reports the conditional correlations between early revenue growth in startups and the factors discussed in Section 2. We regress the early average revenue growth rate (equation 1) on our three broad groups of firm characteristics—first on each individual group, and then on all groups together—controlling for state-by-industry (NAICS 6) and firm age. While controls for owner gender are never statistically significant, we also include them in all specifications.
Column (1) reports estimates for the owner characteristics. Combining rows (1) and (2), having an owner who both holds an advanced degree and previously owned a business is associated with a 4.4-pp higher early-growth rate. Owner age exhibits a monotonic relationship: startups with an owner aged 35 or older have a lower early-growth rate than those with a younger owner, while firms with owners 55 or older demonstrate even less growth. Having a “lifestyle” reason as a very important owner motivation has a negative (though not statistically significant in this model) point estimate.
Column (2) explores startup conditions. VC investment and larger initial capitalization are both associated with higher revenue growth. While rare, VC-funded startups with an initial capital of more than $1 million exhibit a 30-pp higher early-growth rate compared with the omitted groups.
Column (3) reports the coefficients for innovation and business strategies considered together. Each of process and product innovation, IP use, and a growth-oriented business strategy is conditionally associated with higher early growth. This is particularly so for owning a patent (7.7-pp higher early revenue growth) and having a growth-oriented strategy (5.4-pp higher). While both cases are statistically significant, recent innovation in processes has a much stronger connection to early revenue growth than product innovation (nearly 4 pp vs. just over 1 pp).
Column (4) includes all of the owner and firm characteristics together, showing the robustness of the patterns in columns (1)–(3). In addition, the indicator of “lifestyle” reason as being “very important” for starting a business increases in magnitude and becomes significant at the 10% level. Here, controlling for owner characteristics, startup conditions, and innovation/business strategies, an owner who reported a “lifestyle” reason as “very important” for owning the business is associated with a 0.8-pp lower early-growth rate. In column (5), we explore this relationship further by replacing the “lifestyle” reason indicator with indicators for every possible reason covered in the ABS. These indicators are not mutually exclusive and reported in detail in Table 6b. The coefficients on both “Flexible hours” and “Balance work and family” (i.e., the reasons that make up our “lifestyle” indicator) are negative and significant (column 1 of Table 6b),²⁷ while “Best avenue for ideas/goods/services” and “Help and/or become more involved in community” have positive and both statistically and economically significant associations with early growth.

[Page 18]
TABLE 6a Correlates of early firm growth.

| | **(1)** | **(2)** | **(3)** | **(4)** | **(5)** | **(6)** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Description** | **Revenue growth (first 3 years)** | **Revenue growth (first 3 years)** | **Revenue growth (first 3 years)** | **Revenue growth (first 3 years)** | **Revenue growth (first 3 years)** | **Specific industries revenue growth (first 3 years)** |
| Advanced degree (1/0) | 0.0248*** | | | 0.0161** | 0.0167** | 0.0129 |
| | (0.0069) | | | (0.0068) | (0.0068) | (0.0108) |
| Prior business (1/0) | 0.0194*** | | | 0.0094** | 0.0076* | 0.0107 |
| | (0.0045) | | | (0.0045) | (0.0045) | (0.0079) |
| Owner age (35-54) | -0.0463*** | | | -0.0446*** | -0.0428*** | -0.0445*** |
| | (0.0070) | | | (0.0070) | (0.0070) | (0.0134) |
| Owner age (55+) | -0.1009*** | | | -0.0961*** | -0.0937*** | -0.1037*** |
| | (0.0079) | | | (0.0079) | (0.0079) | (0.0151) |
| Lifestyle reason (1/0) | -0.0037 | | | -0.0081* | | |
| | (0.0049) | | | (0.0049) | | |
| Funded by venture capital (1/0) | | 0.1607*** | | 0.1289*** | 0.1276*** | 0.1897*** |
| | | (0.0364) | | (0.0362) | (0.0362) | (0.0633) |
| Startup capitalization 25K-1M (1/0) | | 0.0629*** | | 0.0564*** | 0.0553*** | 0.0965*** |
| | | (0.0051) | | (0.0051) | (0.0051) | (0.0095) |
| Startup capitalization 1M+ (1/0) | | 0.1393*** | | 0.1308*** | 0.1295*** | 0.2109*** |
| | | (0.0173) | | (0.0172) | (0.0172) | (0.0370) |
| Process innovation (1/0) | | | 0.0397*** | 0.0352*** | 0.0328*** | 0.0290*** |
| | | | (0.0056) | (0.0056) | (0.0056) | (0.0096) |
| Product innovation (1/0) | | | 0.0132*** | 0.0100** | 0.0093** | 0.0157** |
| | | | (0.0043) | (0.0043) | (0.0043) | (0.0078) |
| Patents owned or pending (1/0) | | | 0.0773*** | 0.0591*** | 0.0586*** | 0.0621** |
| | | | (0.0207) | (0.0205) | (0.0204) | (0.0312) |
| IP is very important (1/0) | | | 0.0402*** | 0.0327*** | 0.0302*** | 0.0327*** |
| | | | (0.0061) | (0.0061) | (0.0061) | (0.0105) |
| Growth-oriented innovation strategy (1/0) | | | 0.0542*** | 0.0480*** | 0.0402*** | 0.0368*** |
| | | | (0.0047) | (0.0047) | (0.0048) | (0.0084) |
| State-by-industry controls | Yes | Yes | Yes | Yes | Yes | Yes |
| Firm age controls | Yes | Yes | Yes | Yes | Yes | Yes |
| Owner gender controls | Yes | Yes | Yes | Yes | Yes | Yes |
| Reasons for owning controls | No | No | No | No | Yes | Yes |
| **Observations (rounded)** | **75,000** | **75,000** | **75,000** | **75,000** | **75,000** | **28,000** |
| **R²** | **0.227** | **0.229** | **0.230** | **0.237** | **0.238** | **0.228** |

*Notes*: Standard errors in parentheses. Revenue growth refers to the 3-year average of the log-difference measure of annual revenue growth. State-by-industry controls refer to state and six-digit NAICS industry dummies. The underlying sample for columns (1)-(5) is our startup sample (column 4, Table 1). Specific Industries in column (6) refers to the startup sample in specific industries (column 5, Table 1). For a detailed breakdown of "Reasons for Owning Controls" (which replaces "Lifestyle Reason" in columns 5 and 6), please refer to Table 6b.

*Abbreviations*: IP, intellectual property; NAICS, North American Industry Classification System.

*, **, and *** denote significance at 10%, 5%, and 1%, respectively.

[Page 19]
Column (6) of Table 6a examines the same specification, restricting the sample to the four sectors with the highest usage rates of at least one AI-related technology. Restricting attention to manufacturing, information, services, and healthcare (column 5, Table 1) reveals similar patterns, except that holding an advanced degree or previously owning a business does not have statistically significant links to early growth in these already-advanced sectors. As to founding motivations (column 2 of Table 6b), we find similar patterns, except that “Balance work and family” and “Best avenue for ideas/goods/services" are not statistically significant, while pursuing flexible hours seems even more inconsistent with early growth within these more AI-intensive industries.

## 4.3 | Conditional correlates of AI adoption

We next look at how well early growth, itself, predicts AI use in 2017, as well as the extent to which this relationship may be disentangled from the factors explored in Table 6a. Controlling for industry by state, as well as age and gender of the owner, column (1) of Table 7 indicates that higher early growth is positively and significantly associated with AI use.²⁸ A 10-pp increase in the initial 3-year average growth rate is associated with a 0.13-pp increase in the likelihood of using AI—equivalent to a 2.2% increase at the mean usage rate of 6% for the startup sample.

In column (2), we condition on the firm characteristics linked to early growth from Table 6a, beginning with those of the primary owner. Despite these additions, the association between AI use and early revenue growth remains largely unchanged. However, having an owner with an advanced degree is associated with a 1.04-pp increase in the likelihood of using AI (a 17% increase at the mean). AI use is also more likely if the owner previously had another business (1.20 pp). Conditional on education and experience, having an owner aged 55 and up has a significant negative coefficient (−0.92 pp). Lifestyle motivations are not statistically significant in this specification.²⁹

Columns (3) and (4) of Table 7 repeat this exercise, but instead focus on startup financing and location, respectively. The presence of VC funding has a particularly strong relationship to AI use, with a striking 10.7-pp increase in the probability of AI use, absent other controls. Higher startup capitalization, even at the more-modest threshold of $25,000, is also associated with a higher probability of AI use, though this also appears related to the absence of other covariates (see below). The relationship between business location and AI use in column (4) suggests that startups located in large CBSAs have a 0.74-pp higher probability of using AI compared with those located in a micropolitan or rural area with fewer than 50,000 people (the omitted group).

In column (5), we include all previous covariates as well as innovation and business strategies.³⁰ Process innovation, patents, and importance of IP protection have the strongest conditional correlation with AI use, with probability increases of 5.4, 3.5, and 6.1 pp, respectively. Firms with recent product innovation or a growth-oriented strategy were also statistically more likely to be AI users, but at smaller magnitudes and conditional on the other covariates, including early growth and the other measures (contrasting with the large unconditional differences in Table 5). Recall from Table 5 that process innovation and placing importance on IP are distinctly more prevalent in this young-firm sample. Together, these two characteristics are associated with an increase in the probability of AI use of 11.5 pp, nearly twice the average adoption rate.

Also in column (5) of Table 7, the conditional correlation of AI use with urbanization becomes weaker compared with the results in column (4). Conditioning directly on firm-level factors such as beneficial startup conditions and successful innovation appears to explain the otherwise strong-looking link between AI use and the amenities associated with locating in a large CBSA.

Across columns in Table 7, early growth *per se* retains a statistically significant relationship with AI use. However, by column (5) the magnitude falls to less than half of that in column (1). A 10-pp increase in early revenue growth here is associated with only a 0.06-pp increase in probability.

Two observations are in order. The first is that a significant amount of the correlation between early growth and AI use is attributable to firm characteristics associated with growth, not necessarily to growth itself. A key advantage of our study lies in this ability to directly account for factors that have been associated with high-growth entrepreneurship, partialling out their direct relationship to AI use. The second is that the remaining association with early growth is consistent with the possibility that faster-growing startups may have the need and/or resources to adopt and use AI. Taken together, these findings point to greater growth of AI in what have historically been the most dynamic drivers of the aggregate economy.

Overall, this richly specified model explains only 23% of the variation in AI use—an increase of about 10% over the initial specification in column (1). While the firm characteristics included in column (5) contribute significantly to the

[Page 20]
394
-WILEY-
Journal of Economics &
Management Strategy
MCELHERAN ET AL.

TABLE 6b Correlates of early firm growth (detailed reasons for owning business) correspond to columns (5) and (6) in Table 6a.

| Description | (1) <br> Revenue <br> growth <br> (first 3 years) | (2) <br> Specific industries <br> revenue growth <br> (first 3 years) |
| :--- | :--- | :--- |
| Wanted to be own boss (1/0) | 0.0199*** <br> (0.0062) | 0.0291*** <br> (0.0108) |
| Flexible hours (1/0) | -0.0175*** <br> (0.0061) | -0.0303*** <br> (0.0108) |
| Balance work and family (1/0) | -0.0115* <br> (0.0060) | -0.0103 <br> (0.0106) |
| Opportunity for greater income (1/0) | -0.0002 <br> (0.0058) | 0.0015 <br> (0.0094) |
| Best avenue for ideas/goods/services (1/0) | 0.0139*** <br> (0.0052) | 0.0127 <br> (0.0091) |
| Unable to find employment (1/0) | -0.0252*** <br> (0.0081) | -0.0317** <br> (0.0158) |
| Working for someone else not appealing (1/0) | -0.0006 <br> (0.0051) | -0.0052 <br> (0.0092) |
| Always wanted to start own business (1/0) | 0.0105* <br> (0.0054) | 0.0173* <br> (0.0095) |
| Entrepreneurial role model (1/0) | -0.0009 <br> (0.0057) | -0.0138 <br> (0.0107) |
| Carry on family business (1/0) | -0.0029 <br> (0.0076) | 0.0086 <br> (0.0177) |
| Help or become involved in community (1/0) | 0.0212*** <br> (0.0055) | 0.0223** <br> (0.0096) |
| Other reasons (1/0) | 0.0141* <br> (0.0079) | 0.0108 <br> (0.0145) |

Notes: This table breaks out the individual "Reasons for Owning Controls" and directly corresponds to Table 6a. Specifically, column (1) belongs with column (5) in Table 6a and column (2) belongs with column (6) in the same table. Standard errors in parentheses. Revenue growth refers to the 3-year average of the log-difference measure of annual revenue growth. State-by-industry controls refer to state and six-digit NAICS industry dummies. The underlying sample for columns (1)-(5) is our startup sample (column 4, Table 1). Specific Industries in column (6) refers to the startup sample in specific industries (column 5, Table 1).

Abbreviation: NAICS, North American Industry Classification System.

*, **, and *** denote significance at 10%, 5%, and 1%, respectively.

explanatory power of the model, a substantial portion of the variation in AI adoption still remains unexplained, underscoring the large amount of still-unobserved heterogeneity underlying AI diffusion in the United States.

To gain insight, we have sufficient power and coverage to narrow the focus in column (6) to the four leading sectors for AI use (see Figure 2b): manufacturing, information, healthcare, and professional/technical services. Overall patterns remain largely consistent, with a few exceptions. Early growth and having an advanced degree regain predictive power, while owner motivation now stands out as significant. Within these key sectors, AI use was 1.58 pp less likely if the firm was founded or purchased for "lifestyle" reasons. This magnitude is on par with the positive association with early growth, an advanced degree, or product innovation. The latter more than doubles in magnitude within these key sectors, yet it still trails the importance of process innovation, which is associated with a 6.14-pp

[Page 21]
**TABLE 7** Correlates of AI adoption—including early firm growth rate.

| | (1) | (2) | (3) | (4) | (5) | (6) <br> Specific <br> industries | (7) <br> Full owner <br> and revenue <br> sample |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Description** | **Use AI** | **Use AI** | **Use AI** | **Use AI** | **Use AI** | **Use AI** | **Use AI** |
| Revenue growth (first 3 years) | 0.0134*** <br> (0.0024) | 0.0128*** <br> (0.0024) | 0.0112*** <br> (0.0024) | 0.0133*** <br> (0.0024) | 0.0058** <br> (0.0024) | 0.0150*** <br> (0.0045) | 0.0021 <br> (0.0016) |
| Revenue growth (last 3 years) | | | | | | | 0.0041** <br> (0.0018) |
| Advanced degree (1/0) | | 0.0104*** <br> (0.0032) | | | 0.0043 <br> (0.0031) | 0.0159*** <br> (0.0054) | 0.0087*** <br> (0.0018) |
| Prior business (1/0) | | 0.0120*** <br> (0.0023) | | | 0.0066*** <br> (0.0023) | 0.0081* <br> (0.0047) | 0.0050*** <br> (0.0013) |
| Owner age (35-54) | | -0.0029 <br> (0.0034) | | | 0.0016 <br> (0.0033) | 0.0046 <br> (0.0069) | 0.0004 <br> (0.0026) |
| Owner age (55+) | | -0.0092** <br> (0.0038) | | | -0.0019 <br> (0.0038) | 0.0008 <br> (0.0078) | -0.0014 <br> (0.0027) |
| Lifestyle reason (1/0) | | -0.0004 <br> (0.0024) | | | -0.0032 <br> (0.0024) | -0.0158*** <br> (0.0052) | -0.0021 <br> (0.0013) |
| Funded by venture capital (1/0) | | | 0.1071*** <br> (0.0161) | | 0.0862*** <br> (0.0156) | 0.1048*** <br> (0.0254) | 0.0578*** <br> (0.0101) |
| Startup capitalization 25K-1M (1/0) | | | 0.0148*** <br> (0.0028) | | 0.0078*** <br> (0.0027) | 0.0121** <br> (0.0058) | 0.0090*** <br> (0.0015) |
| Startup capitalization 1M+ (1/0) | | | 0.0297*** <br> (0.0078) | | 0.0139* <br> (0.0078) | 0.0129 <br> (0.0159) | 0.0130*** <br> (0.0044) |
| Process innovation (1/0) | | | | | 0.0544*** <br> (0.0034) | 0.0614*** <br> (0.0062) | 0.0574*** <br> (0.0020) |
| Product innovation (1/0) | | | | | 0.0078*** <br> (0.0022) | 0.0197*** <br> (0.0045) | 0.0090*** <br> (0.0012) |
| Patents owned or pending (1/0) | | | | | 0.0353*** <br> (0.0115) | 0.0361** <br> (0.0160) | 0.0329*** <br> (0.0064) |
| IP is very important (1/0) | | | | | 0.0605*** <br> (0.0037) | 0.0656*** <br> (0.0063) | 0.0572*** <br> (0.0021) |
| Growth-oriented innovation strategy (1/0) | | | | | 0.0066*** <br> (0.0023) | 0.0058 <br> (0.0047) | 0.0091*** <br> (0.0012) |
| Small CBSA | | | | -0.0006 <br> (0.0043) | -0.0007 <br> (0.0043) | -0.0010 <br> (0.0101) | 0.0003 <br> (0.0022) |
| Medium CBSA | | | | 0.0003 <br> (0.0036) | -0.0010 <br> (0.0036) | 0.0087 <br> (0.0082) | -0.0004 <br> (0.0019) |
| Large CBSA | | | | 0.0074** <br> (0.0031) | 0.0042 <br> (0.0031) | 0.0075 <br> (0.0070) | 0.0013 <br> (0.0017) |

(Continues)

[Page 22]
TABLE 7 (Continued)
| | (1) | (2) | (3) | (4) | (5) | (6) Specific industries | (7) Full owner and revenue sample |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Description** | **Use AI** | **Use AI** | **Use AI** | **Use AI** | **Use AI** | **Use AI** | **Use AI** |
| State-by-industry controls | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Firm age controls | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Owner gender controls | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Observations (rounded) | 75,000 | 75,000 | 75,000 | 75,000 | 75,000 | 28,000 | 209,000 |
| R² | 0.209 | 0.210 | 0.211 | 0.209 | 0.230 | 0.228 | 0.148 |

Notes: Standard errors in parentheses. Revenue growth refers to the 3-year average of the log-difference measure of annual revenue growth. “Use” is defined as having responded with “In use for less than 5% of production or service,” “In use for between 5%–25% of production or service,” or “In use for more than 25% of production or service” for the category listed on any of the AI-based Business Technologies (Automated-Guided Vehicles, Natural Language Processing, Machine Learning, Machine Vision, and Voice Recognition). State-by-industry controls refer to state-specific six-digit NAICS industry dummies. The underlying sample for columns (1)–(5) is our startup sample (column 4, Table 1). Specific Industries in column (6) refers to the startup sample in specific industries (column 5, Table 1). Full owner and revenue sample in column (7) refers to our owner and revenue sample (column 3, Table 1). Column (7) is identical to column (5) of Table A4, which contains columns similar to this table for the full owner and revenue sample.

Abbreviations: AI, artificial intelligence; CBSA, core-based statistical area; IP, intellectual property; NAICS, North American Industry Classification System. *, **, and *** denote significance at 10%, 5%, and 1%, respectively.

increased likelihood of AI use. On net, while many patterns remain robust to this shift in focus, it further underscores the importance of industry context in AI adoption.

Finally, we widen the focus in column (7) to include the somewhat older firms for which we have both owner and revenue data, recognizing the sample limitations imposed by data availability (see column 3, Table 1 and Data Appendix B). Extending the sample back to 1997, we can include not only the average revenue growth for the initial years of the firm, but also the average revenue growth rate from the 3 most recent years for which revenue information is available, 2016–2018. (While we report the complete set of results for this sample in the appendix Table A4, we report the fullest specification in column 7 of Table 7.) In this sample of around 209,000 firms, the coefficient on early revenue growth weakens and loses significance with the inclusion of owner characteristics, startup conditions, and innovation and business strategies. Instead, the coefficient on later-stage revenue growth is statistically significant and with a magnitude that, while small (a 10-pp increase in later-stage revenue would be associated with a 0.04-pp increase in the likelihood of AI use), is on par with factors such as prior founding experience and greater than the effects associated with product innovation or growth-oriented business strategy.

This later period of revenue growth more likely falls into the postadoption period for many (largely older) firms, suggesting that the use of AI itself could have contributed to the performance of the firms that put it to use. A few caveats are in order, however. First, this will largely hold for very early adopters. On the basis of the patterns we observe in 2017, these are likely to be larger firms, even among the privately held firms we examine in depth. In addition, we do not observe the adoption year, only whether or not AI was being used as of 2017; thus, we cannot establish a credible causal link. That said, it is interesting to observe the statistically significant relationship between later-stage revenue growth and AI use in such a large sample, while seeing the coefficient on early revenue growth lose significance once we account for its links to owner characteristics, startup conditions, and innovation and business strategies

# 5 | SUMMARY OF KEY FINDINGS AND DISCUSSION

This paper describes a rich snapshot of the who, what, and where of early AI use across the US economy. Leveraging the largest and most-detailed data collection to date concerning firm use of AI in production, the sheer breadth and depth of the data yield a number of novel facts about the early reach and potential of AI. Here, we distill our findings into a handful of core themes, including some discussion of limitations and implications for future work.

[Page 23]
## **5.1 | Diffusion of AI is low yet concentrated in key segments of the economy**

Overall, the view of early AI use among US firms is one of low average diffusion, yet with higher concentration in
certain sectors, very large firms, and higher-growth startups. While average firm adoption in 2017 was only 5.8%, this
rises to 18.2% with employment weighting. This gap suggests that understanding worker-level impacts will likely
require more attention to firms and their competitive dynamics, moving beyond a skill- or task-based view.

These adoption rates are much lower than other studies lacking the representation and coverage of our data, particularly
with respect to smaller and medium-sized firms. This matters because, while we do not directly observe impediments to AI
adoption, scale (or lack thereof) clearly plays a role. Indeed, these low average rates risk obscuring the fact that most very
large firms (more than 5000 employees) report at least some AI use, as well as higher intensity of use.

This pattern of low yet skewed early AI adoption further has important implications for its trajectory. Low actual
use in production—despite significant “hype” in the popular press—likely reflects nontrivial frictions in putting these
innovations to work in practice (e.g., Agrawal et al., 2023; Bresnahan, 2019, 2023). Yet large firms disproportionately
overcame these challenges early on, and scale advantages tend to be self-reinforcing. Thus, early disparities could fuel
an “AI divide” if such patterns persist.

That said, our analysis of startups reveals a strong conditional correlation between AI use and a direct measure of
recent process innovation at the firm. This points specifically to process-level frictions that are being overcome—and,
moreover, not only among “superstar” firms. Our study's most-detailed insights are most robust for younger firms,
however, leaving open questions concerning the adaptation and adjustment activities of larger and older incumbents
for future study.

Overall, our detailed exploration into AI use among startups reveals early AI use concentrated among the types of
firms—innovative, with high-growth potential—that matter most for economic growth and dynamism. Their rising
participation in the economy may fuel greater diffusion and impact of AI, potentially challenging existing patterns of
concentration or contributing benefits alongside the much-discussed risks of AI use. Our findings, while stopping short
of sharp predictions, point to a number of key areas of both concern and potential in need of future exploration.

## **5.2 | Technology characteristics and interdependencies matter**

While the goal of this study is not to take a stand on whether AI is a “general-purpose technology” or GPT (Bresnahan
& Trajtenberg, 1995; Cockburn et al., 2019; Goldfarb et al., 2023; Trajtenberg, 2018), our findings contribute to this
discussion. The first is documenting its breadth of use: early use of AI in production spanned all sectors of the
economy. Broad, general use of influential technologies typically requires uptake within the application-producing
sectors (Bresnahan, 2023), which we also find in our early baseline measures (e.g., among medical labs and software
publishers).

AI use further appears alongside other high-potential technologies such as cloud computing and robotics, as well as
building on the presence of digitally stored information (i.e., data) within firms. Clustered use of emerging technologies
has historically been an essential step in technology-driven waves of growth (Rosenberg, 1963), yet this involves key
tradeoffs. On the one hand, high co-occurrence of “enabling” technologies may reinforce the advantages of more
digitally advanced firms. On the other hand, complementarities among fast-evolving digital resources may entail higher
costs of adoption and “coinvention” (Bresnahan & Greenstein, 1996), a known challenge for market leaders
(McElheran, 2015). Taken together, such competing mechanisms tend to promote unevenness in the returns to novel
technologies, as observed in prior waves of digital transformation (e.g., Brynjolfsson, Jin, et al., 2021; Brynjolfsson &
McElheran, 2016). As our data lack direct measures of the costs of adopting any of these technologies, a priority for
future work is understanding both drivers of and heterogeneity in AI adoption costs.

## **5.3 | Firms associated with “high-growth” entrepreneurship adopt AI**

Our interest in firm dynamics led us to examine AI use more closely in a large sample of young firms. Among startups,
early indicators of high-growth potential were not only validated by empirically linking them to actual revenue growth
in the administrative data, but they also shed considerable light on AI use. Factors associated with high-growth
“gazelles” (VC funding, owning patents, and high startup capitalization) had the largest marginal association with AI

[Page 24]
use. One interpretation is that high-potential firms have advantages that also promote or better-leverage AI use;
however, we do not rule out reverse causality, such as VC influence in promoting AI adoption.
Also as part of our interest in young high-potential firms, we explored the role of firm leaders and their
characteristics in AI adoption. This revealed that more-educated, more-experienced, and younger owners (typically
founders) were more likely to preside over AI adoption at their firms, even controlling for other markers of early
growth (and other factors, such as geography and industry).
These stylized facts, alongside our finding that the motivations of owners and founders predicted early AI use,
provide novel insights into the literature on technology diffusion and its implications. We documented, first, that high-
growth and innovative firms were often led not only by individuals motivated by bringing new ideas to market, but also
by those who embraced prosocial values such as helping or becoming involved in the community. In turn, such
motivations dominated so-called “lifestyle” entrepreneurship when it came to AI use. This again suggests an outsized
impact of AI compared with its low early average adoption, while pointing to potential guardrails regarding its specific
applications in practice. This will be an important focus for follow-on work, as concerns rise about AI safety and ethics.

## **5.4 | Firm strategies matter for AI use**

Innovation and growth-oriented business strategies, also difficult to observe at scale, significantly predicted both early
revenue growth and AI use. While process innovation overshadows product innovation as a predictor of AI use,
product innovation and reliance on formal IP are key correlates of startup use of AI (despite their high baseline
prevalence and conditioning on a large number of other early-growth indicators). Growth-oriented strategy has a
smaller but nevertheless significant correlation with AI use, even conditioning on actual early revenue growth.
Indeed, conditioning directly on a large number of markers of high-growth potential reveals a robust relationship
between AI use and growth per se among startups. A possible interpretation is that firms with a demonstrated upward
trajectory from early on may have both a greater demand and the requisite resources and organizational complements
to exploit AI. Even so, our analysis of startups, as well as of a broader set of firms for which we can assess revenue
growth later in life, both point to an important relationship between growth and adoption that is consistent with
performance gains due to AI use. That said, establishing causality is beyond the scope of our study, and we hope that
these findings may provide the foundation for follow-on efforts to understand causality between AI use and firm
performance.

## **5.5 | Geographic disparity in the adoption of AI is pronounced**

Our fifth main theme is substantial geographic concentration in the adoption and use of AI. Consistent with our in-
depth exploration of young firms above, our findings emphasize key hubs of AI use among startups. We find the rate of
AI use to be higher in CBSAs located in the southern and western parts of the United States. Concentration in known
technology hubs (Bloom et al., 2021; Kerr & Robert-Nicoud, 2020), such as Silicon Valley and the Research Triangle, is
consistent with clustering of job postings relating to AI and the importance of proximity to academic centers (e.g.,
Bessen et al., 2021; Bloom et al., 2021; Muro & Liu, 2021). Yet certain large metro areas, such as Nashville, San Antonio,
Las Vegas, New Orleans, San Diego, and Tampa, also show high concentrations of AI use. The concentration of AI in
already-leading locations suggests an “AI divide" that may be further reinforced if new AI-using, high-growth startups
continue to be attracted to locations with already-high-AI activity.
Of note, our ranking of AI clusters overlaps incompletely with prior studies. While uncovering specific drivers of
early AI geography is beyond the scope of our study, our interpretation is that the forces promoting agglomeration in
use may be distinct from those promoting co-location for invention or early commercialization, as identified in
measures based on patents, publications, and/or demand for AI-related skills. Further, when we weight by
employment, a number of less-obvious locales (primarily in the Midwest and Mid-Atlantic) attain prominence.
Discussions around the "future of work" as AI diffuses may need to address different considerations for firms seeking
to develop or supply AI-related technologies, versus those whose production activities and sheer size expose a broader
range and number of employees to AI at work.

[Page 25]
## 5.6 | Characterizing AI adoption poses a significant measurement challenge

While not one of our five main stylized facts, a consideration that runs throughout our study is the recognition that typically observable firm characteristics leave unexplained a large fraction of the variation in AI adoption across firms. Even with high-dimensional controls (state-industry controls at the six-digit NAICS level), along with controls for firm age and owner gender, we can only explain around 21% of the variation in adoption (see Table 7). This low explanatory power despite detailed covariates indicates that significant unobserved heterogeneity remains in AI adoption among US firms. Including additional, harder-to-measure factors from the ABS related to leadership, capitalization, and innovative strategies contributes significantly to the explanatory power (an increase of about 10% from the baseline specification). Nevertheless, a large amount of variation is left unexplained, underscoring the importance of idiosyncratic firm-level unobserved factors, such as the specific product or service being offered by a firm or the types of processes and tasks used in production. This points to a number of important areas for follow-on data collection and research, as well as the recognition that choices taken around measurement and sample composition may have significant implications for inference.

# 6 | CONCLUSION

As AI advances and becomes more integrated into the workplace, there is a growing debate about whether it will increase productivity, what the effects on the workforce will be, or even whether AI will spark a revolution in business processes and models. Central to these debates is obtaining reliable measures of AI use across the US firm population, identifying relevant adopter characteristics, and assessing worker exposure to AI.

The 2018 ABS technology module addresses this data need along a number of dimensions, providing detailed information about the early diffusion of AI and related technologies across a nationally representative set of firms, further linked to detailed information on industry, age, and revenue over the firm life cycle. It further provides unprecedented insights into the technological and organizational context of AI use, particularly among high-potential US startups.

As touched on throughout, our study is not without limitations. While our "headline" adoption statistics are robust and unusually representative of the entire US economy, our most-nuanced characterization of AI users leans on a particular subsample of young firms. This sample is large and covers important swaths of the firm size and industry distributions, yet it is also subject to nontrivial ownership and age restrictions. Ultimately, our approach trades off unusual visibility to early-stage entrepreneurial activity—as well as changes across the life cycle-for insights that may be less applicable to the publicly traded firms predominant in related studies. To the extent that we seek to signpost AI's future trajectory, in addition to documenting its early baseline, we argue this tradeoff is worth making. Our findings are also conditional on survival: any firms that adopted AI and failed before 2018 are missing from our study³¹ (a common limitation in observational data).

The exploration of AI's leading edge provided here arguably raise more questions than they answer. Among the many patterns we document, the potential for an “AI divide" between different types of firms and geographies is visible—and in need of careful assessment. Pinning down causal relationships is also beyond the reach of this first cross-section of early data. Our hope is that future collections can build a panel of stable measures and identify exogenous variation in AI use for this important endeavor. That said, the patterns we uncover concerning the who, what, and where of early adoption of AI may support a more evidence-based response to current technological advances and economic challenges and identify promising paths for future work.

# ACKNOWLEDGMENTS

Any opinions and conclusions expressed herein are those of the authors and do not represent the views of the U.S. Census Bureau. This study relies on confidential microdata available to approved projects through the U.S. Federal Statistical Research Data Centers. All results have been reviewed to ensure that no confidential information is disclosed. The Census Bureau has reviewed this data product to ensure appropriate access, use, and disclosure avoidance protection of the confidential source data (Project No. P-7508509, Disclosure Review Board [DRB] approval number: CBDRB-FY20-095, CBDRB-FY20-331, CBDRB-FY21-041, CBDRB-FY22-074, CBDRB-FY22-246, and CBDRB-FY23-0309). We thank the Editor, Dan Spulber, Associate Editor Feng Zhu, two anonymous referees, Tim Bresnahan, John Eltinge, Nathan Goldschlag, Rob Seamans, and seminar participants at Georgetown University McDonough

[Page 26]
School of Business for excellent comments and feedback. Financial support from the Stanford Digital Economy Lab, the Ewing Marion Kauffman Foundation and the Social Sciences and Humanities Research Council (SSHRC) of Canada is gratefully acknowledged.

## DATA AVAILABILITY STATEMENT
This study relies on confidential microdata available to approved projects through the U.S. Federal Statistical Research Data Centers. All results have been reviewed to ensure that no confidential information is disclosed.

## ORCID
Kristina McElheran http://orcid.org/0000-0003-0844-4901

## ENDNOTES
1. For reference, the quinquennial Economic Census typically has a response rate of approximately 80% for single-unit firms (Dinlersoz & Klimek, 2011). The Community Innovation Survey in Europe reported response rates of 25%–35% in Germany, resulting in approximately 5.5 thousand firms (Czarnitzki et al., 2023). The Eurostat survey of AI had response rates of 5%–19% across 27 EU countries, yielding over 9.6 thousand firms (Hoffreumon et al., 2023).
2. AI-related technologies are actually quite diverse. The ones covered in the ABS are: AGVs, machine learning, machine vision, natural language processing, and voice recognition. See Table 2. To best capture the extensive margin of AI use across industries, we combine usage rates across AI-related technologies. That said, our findings largely represent variation in the use of “machine learning” in production.
3. Young firms are disproportionately single-unit, and hence straightforward to situate geographically.
4. Studies of AI use and impacts outside of the United States have been on the rise, including in Europe (Czarnitzki et al., 2023; Hoffreumon et al., 2023), China (Beraja et al., 2023; Lu et al., 2023), Canada (Alexopoulos & Cohen, 2018), and in the context of international trade (Brynjolfsson et al., 2019; Goldfarb & Trefler, 2019).
5. See also Alcacer and Delgado (2016), Delgado et al. (2010), and Forman et al. (2005), inter alia.
6. For example, Akcigit et al. (2022), Botelho et al. (2021), Catalini et al. (2019), and Lerner and Nanda (2020).
7. See Brynjolfsson and Milgrom (2013) for more on complementarity theory and a review of the literature.
8. Such details are captured via responses from “primary owners” to the ABS, which excludes publicly traded firms, estates, trusts, government and tribal entities, associations, membership clubs, cooperatives and foreign entities.
9. Specifically, we recalculate the sample weights by stratifying the firms in the 2017 LBD and our final sample of firms in the ABS on firm size, age, and industry. These strata are defined by the 19 two-digit NAICS sectors and the 12 firm size and 12 firm age groups used in the BDS. We weight according to these more standard firm characteristics because of the unique sampling frames of the ABS (see Section B.1 in our data appendix).
10. Distributions taken from Zolas et al. (2020) show that nearly 70% of ABS firms, and more than 3/4 once weighted, have fewer than 10 employees, while the age distribution is more uniform.
11. Other technologies queried include augmented reality, robotics, touchscreens, automated storage and retrieval systems, and radio frequency identification. While some of these technologies may also contain an AI-related component, they are less likely to rely heavily on AI compared with the ones we consider to be AI-intensive. For instance, the 2018 ABS definition of robotics (a technology that has increasingly relied on AI in recent years) does not mention autonomy, but rather only reprogrammability (i.e., “traditional” industrial robots).
12. Also, the rates of missing data vary by specific technology, which would affect the denominator in calculating rates.
13. The rise in usage rates with firm size could be partly a “mechanical” function of scale. If we conceptualize larger firms as random collections of smaller ones and extrapolate usage rates as a function of number of employees, we would expect even higher usage rates among larger firms.
14. For example, this controls for the distinction between manufacturing hardwood versus softwood veneer (NAICS 321,211 vs. 321,212) and bicycles versus armored vehicles and tanks (336,991 vs. 336,992); newspaper publishers versus greeting card publishers (513,110 vs. 514,191); and casino hotels versus bed-and-breakfast inns (721,120 vs. 721,191).
15. Since the LBD only extends back to 1976, the age distribution in our samples is truncated from above at 42 years, with all firms of age 42+ being assigned to the highest age percentile group. As a result, the coefficient for the highest age percentile should be interpreted with caution.
16. We see similar patterns of increasing overlap as firms get larger. Figure A1 plots the share of AI and robotics adopters across the different size categories. Among AI adopters, the share of firms also adopting robotics rises with size. However, somewhat

[Page 27]
interestingly, we find the opposite pattern among robotics adopters. The share of robotics users that also use AI declines from 65.6%
of robotics adopters in the smallest size category to less than half (49.3%) of firms with 20 or more employees. These patterns
suggest that any underlying complementarities between AI and other technologies may have complex interactions with firm
characteristics, such as scale.

17 This subsample is restricted to firms with information on the primary owner, thus necessarily excluding any publicly owned firms. For
most analyses involving these measures, we further require revenue information. Column (3) of Table 1 describes the relevant
subsample, which is contingent on a successful match to the LBD and its introduction of revenue data in 1997. This excludes firms that
were older than 20 as of 2017. These limitations notwithstanding, the coverage and size of the data set (209,000 firms), along with its
focus on the use of AI in production, are significant in this literature. See Section 2 for details and references, as well as Section B.2 of our
data appendix.

18 For instance, in row (6), only 24.7% of such owners were 55 years or older (column 2), compared with 26.6% of the overall startup sample
(column 1). That said, roughly 55% of all startups (AI using or otherwise) fell in the 35–54 range bracketing “peak entrepreneurship”
(Azoulay et al., 2020).

19 CBSAs are geographic areas consisting of one or more counties (or equivalents) with an urban center of at least 10,000 people plus
adjacent counties that are socioeconomically tied to the urban center by commuting. For multiunit firms in this “startup subsample,” we
assign a single CBSA by taking the maximum employment within a firm-zip code.

20 Because a sample of single-unit firms differs somewhat from our nationally representative baseline sample, we modify our firm weights.
We do not, however, directly incorporate geographic information when generating our weights. For comments on incorporating
geography into tabulation weights, see Section B.3 in our data appendix.

21 Because we only require location information, this sample includes startups that do not appear in our core startup sample from column
(4), Table 1. However, because of the granularity of CBSAs and to protect confidentiality, we only report information for the 30,000
startups in the largest CBSAs (i.e., those with a population of one million or more).

22 Because Durham–Chapel Hill does not meet our population requirement to be designated as a “large” CBSA, this piece of the Research
Triangle is absent from Figure 5 and Table A2. However, Figure A3a shows that Durham–Chapel Hill has a relatively high usage rate of
AI when considering all single-unit firms.

23 This is consistent with work by Muro and Liu (2021) which found the job postings relating to AI are similarly clustered, and with Bloom
et al. (2021) and Bessen et al. (2021) which found that proximity to academic centers was important.

24 We perform a similar analysis for all single-unit firms across 350+ CBSA categories (of all sizes—not just the largest) for which at least 20
single-unit AI firms exist. These can be found in the appendix Figure A3a,b. The results are qualitatively similar but with some
interesting patterns of dispersion among the small and midsized CBSAs.

25 These shifts can be attributed to a variety of factors. For instance, certain locations have a few young AI users that are relatively large
compared with others in the same location, whereas in other locations AI-using single-unit firms may be numerous yet too small to
make up a large share of employment. Differences in industrial composition also matter. For instance, manufacturing is a leading
AI-using industry (Figure 2b), leading large AI-using manufactures clustered in the Midwest to receive greater weight, despite
comprising a small fraction of their CBSA's total single-unit startups.

26 This analysis restricts on firms that survived through 2017 and responded to the survey in 2018: differential survival rates of adopters
versus nonadopters before 2017 would introduce biases whose sign is difficult to predict. That said, most studies of technology adoption
and the impact of impact technology on performance are vulnerable to this concern (see Jin & McElheran, 2017 for a discussion and
evidence).

27 “Unable to find employment” is also negative, statistically significant, and relatively large in magnitude. However it has little explanatory
power in the AI usage regressions, to follow. A similar lack of explanatory power shows up for “Wanted to be own boss,” so we abstract
away from these in our core analyses.

28 Recall that we do not claim a causal relationship. In fact, faster-growing startups may be more able to use and benefit from AI if the
initial costs of adoption or the scale of training data are large.

29 As described in Section 3.6.1, we find (unconditionally) that the use of AI-related technologies is negatively correlated with
“Flexible hours” and “Balance work and family” reasons, and it is positively correlated with “Best avenue for ideas/goods/services”
and “Help and/or become more involved in community” (Table A3). For simplicity we thus retain our “lifestyle” reason indicator in
Table 7.

30 This set of covariates, examined on their own analogous to columns (2)–(4), yield nearly identical effects and hence are combined, here,
for brevity.

31 This limitation is common in digital technology research and underscores the importance of collecting data on new technologies as early
as possible (e.g., McElheran, 2018).

[Page 28]
# REFERENCES
Acemoglu, D., Akcigit, U., Alp, H., Bloom, N., & Kerr, W. (2018). Innovation, reallocation, and growth. American Economic Review, 108(11), 3451-3491.

Acemoglu, D., Autor, D., Hazell, J., & Restrepo, P. (2022). Artificial intelligence and jobs: Evidence from online vacancies. Journal of Labor Economics, 40(S1), S293-S340.

Acemoglu, D., & Restrepo, P. (2020). The wrong kind of AI? Artificial intelligence and the future of labour demand. Cambridge Journal of Regions, Economy and Society, 13(1), 25-35.

Agrawal, A., Gans, J., & Goldfarb, A. (Eds.). (2019). The economics of artificial intelligence: An agenda. University of Chicago Press.

Agrawal, A., Gans, J. S., & Goldfarb, A. (2023). Artificial intelligence adoption and system-wide change. Journal of Economics & Management Strategy. Advance online publication.

Akcigit, U., Dinlersoz, E., Greenwood, J., & Penciakova, V. (2022). Synergizing ventures. Journal of Economic Dynamics and Control, 143, 104427.

Alcacer, J., & Delgado, M. (2016). Spatial organization of firms and location choices through the value chain. Management Science, 62(11), 3213-3234.

Alekseeva, L., Azar, J., Giné, M., Samila, S., & Taska, B. (2021). The demand for AI skills in the labor market. Labour Economics, 71(C), 102002.

Alexopoulos, M., & Cohen, J. (2018). Canadian productivity growth, secular stagnation, and technological change. International Productivity Monitor, (35), 113-137.

Aral, S., Brynjolfsson, E., & Wu, L. (2012). Three-way complementarities: Performance pay, human resource analytics, and information technology. Management Science, 58(5), 913-931.

Autor, D., Dorn, D., Katz, L. F., Patterson, C., & Reenen, J. V. (2020). The fall of the labor share and the rise of superstar firms ["Automation and new tasks: How technology displaces and reinstates labor"]. The Quarterly Journal of Economics, 135(2), 645-709.

Azoulay, P., Jones, B. F., Kim, J. D., & Miranda, J. (2020). Age and high-growth entrepreneurship. American Economic Review: Insights, 2(1), 65-82.

Babina, T., Fedyk, A., He, A., & Hodson, J. (2024). Artificial intelligence, firm growth, and product innovation. Journal of Financial Economics, 151, 103745.

Barth, E., Davis, J. C., Freeman, R. B., & McElheran, K. (2023). Twisting the demand curve: Digitalization and the older workforce. Journal of Econometrics, 233(2), 443-467.

Beraja, M., Kao, A., Yang, D. Y., & Yuchtman, N. (2023). Ai-tocracy. The Quarterly Journal of Economics, 138(3), 1349-1402.

Bessen, J., Cockburn, I., & Hunt, J. (2021). Is distance from innovation a barrier to the adoption of artificial intelligence? [Boston University Working Paper].

Bessen, J., Impink, S. M., Reichensperger, L., & Seamans, R. (2022). The role of data for AI startup growth. Research Policy, 51(5), 104513.

Bloom, N., Hassan, T. A., Kalyani, A., Lerner, J., & Tahoun, A. (2021). The diffusion of disruptive technologies (Technical Report). National Bureau of Economic Research.

Bloom, N., Sadun, R., & Van Reenen, J. (2012). Americans do it better: US multinationals and the productivity miracle. American Economic Review, 102(1), 167-201.

Botelho, T. L., Fehder, D., & Hochberg, Y. (2021). Innovation-driven entrepreneurship [NBER Working Papers 28990]. National Bureau of Economic Research Inc.

Bresnahan, T. (2019). Artificial intelligence technologies and aggregate growth prospects. In: J. W. Diamond & G. R. Zodrow (eds.), Prospects for Economic Growth in the United States (pp.132-172).

Bresnahan, T. (2023). What innovation paths for AI to become a GPT? Journal of Economics & Management Strategy. Advance online publication.

Bresnahan, T. F., Brynjolfsson, E., & Hitt, L. M. (2002). Information technology, workplace organization, and the demand for skilled labor: Firm-level evidence. The Quarterly Journal of Economics, 117(1), 339-376.

Bresnahan, T., & Greenstein, S. (1996). Technical progress and co-invention in computing and in the uses of computers. Brookings Papers on Economic Activity: Microeconomics, 1996, 1-83.

Bresnahan, T. F., & Trajtenberg, M. (1995). General purpose technologies 'engines of growth'? Journal of Econometrics, 65(1), 83-108.

Brynjolfsson, E. (2022). The turing trap: The promise & peril of human-like artificial intelligence. Daedalus, 151(2), 272–287.

Brynjolfsson, E., & Hitt, L. (1996). Paradox lost? Firm-level evidence on the returns to information systems spending. Management Science, 42(4), 541-558.

Brynjolfsson, E., & Hitt, L. M. (2000). Beyond computation: Information technology, organizational transformation and business performance. Journal of Economic Perspectives, 14(4), 23-48.

Brynjolfsson, E., Hui, X., & Liu, M. (2019). Does machine translation affect international trade? Evidence from a large digital platform. Management Science, 65(12), 5449-5460.

Brynjolfsson, E., Jin, W., & McElheran, K. (2021). The power of prediction: Predictive analytics, workplace complements, and business performance. Business Economics, 56(4), 217-239.

Brynjolfsson, E., & McElheran, K. (2016). The rapid adoption of data-driven decision-making. American Economic Review, 106(5), 133–139.

Brynjolfsson, E., & McElheran, K. (2019). Data in action: Data-driven decision making and predictive analytics in us manufacturing [Rotman School of Management Working Paper, 3422397].

[Page 29]
Brynjolfsson, E., & Milgrom, P. (2013). Complementarity in organizations. In R. Gibbons & J. Roberts (eds.), *The handbook of organizational economics* (pp. 11–55). Princeton University Press.
Brynjolfsson, E., Mitchell, T., & Rock, D. (2018). What can machines learn, and what does it mean for occupations and the economy? *AEA Papers and Proceedings*, *108*, 43–47.
Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J-curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics*, *13*(1), 333–372.
Camuffo, A., Gambardella, A., & Pignataro, A. (2023). Framing strategic decisions in the digital world. *Strategic Management Review*, *4*(2), 127–160.
Cassar, L., & Meier, S. (2018). Nonmonetary incentives and the implications of work as a source of meaning. *Journal of Economic Perspectives*, *32*(3), 215–238.
Catalini, C., Guzman, J., & Stern, S. (2019). *Hidden in plain sight: Venture growth with or without venture capital* [NBER Working Papers 26521]. National Bureau of Economic Research Inc.
Chari, V. V., & Hopenhayn, H. (1991). Vintage human capital, growth, and the diffusion of new technology. *Journal of Political Economy*, *99*(6), 1142–1165.
Chow, M. C., Fort, T. C., Goetz, C., Goldschlag, N., Lawrence, J., Perlman, E. R., Stinson, M., & White, T. K. (2021). *Redesigning the longitudinal business database* [Working Paper 28839]. National Bureau of Economic Research.
Chui, M., & Malhotra, S. (2018). AI adoption advances, but foundational barriers remain. Mckinsey and Company.
Cockburn, I. M., Henderson, R., & Stern, S. (2019). The impact of artificial intelligence on innovation. In: A. Agrawal, J. Gans, & A. Goldfarb (eds.), *The Economics of Artificial Intelligence: An Agenda*, 115–152.
Cohen, W. M., & Klepper, S. (1996). Firm size and the nature of innovation within industries: The case of process and product R&D. *The Review of Economics and Statistics*, *178*(2), 232–243.
Cowgill, B., & Tucker, C. E. (2020). Algorithmic Fairness and Economics.
Czarnitzki, D., Fernández, G. P., & Rammer, C. (2023). Artificial intelligence and firm-level productivity. *Journal of Economic Behavior and Organization*, *211*, 188–205.
Decker, R. A., Haltiwanger, J., Jarmin, R. S., & Miranda, J. (2017). Declining dynamism, allocative efficiency, and the productivity slowdown. *American Economic Review*, *107*(5), 322–326.
Delgado, M., Porter, M. E., & Stern, S. (2010). Clusters and entrepreneurship. *Journal of Economic Geography*, *10*(4), 495–518.
Deloitte. (2018). *State of AI in the enterprise*.
Dinlersoz, E., Goldschlag, N., Myers, A., & Zolas, N. (2021). An anatomy of US firms seeking trademark registration. In C. Corrado, J. Haskel, J. Miranda, & D. Sichel (eds.), *Measuring and accounting for innovation in the twenty-first century* (NBER Chapters, pp. 183–228). National Bureau of Economic Research Inc.
Dinlersoz, E., Goldschlag, N., Yorukoglu, M., & Zolas, N. (2023). *On the role of trademarks: From micro evidence to macro outcomes* [Center for Economic Studies Working Paper 23-16]. U.S. Census Bureau.
Dinlersoz, E., & Klimek, S. (2011). *Modeling single establishment firm returns to the 2007 economic census* [Working Paper CES-WP-11-28]. U.S. Census Bureau.
Dinlersoz, E., & Wolf, Z. (2018). *Automation, labor share, and productivity: Plant-level evidence from U.S. manufacturing* [Working Papers 18-39]. Center for Economic Studies, U.S. Census Bureau.
Dixon, J., Hong, B., & Wu, L. (2021). The robot revolution: Managerial and employment consequences for firms. *Management Science*, *67*(9), 5586–5605.
Eloundou, T., Manning, S., Mishkin, P., & Rock, D. (2023). GPTs are GPTs: An early look at the labor market impact potential of large language models. *arXiv preprint arXiv:2303.10130*.
Feigenbaum, J. J., & Gross, D. P. (2021). *Organizational frictions and increasing returns to automation: Lessons from AT&T in the twentieth century* (Technical Report). National Bureau of Economic Research.
Felten, E., Raj, M., & Seamans, R. (2021). Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses. *Strategic Management Journal*, *42*(12), 2195–2217.
Forman, C., Goldfarb, A., & Greenstein, S. (2005). How did location affect adoption of the commercial internet? Global village vs. urban leadership. *Journal of Urban Economics*, *58*(3), 389–420.
Forman, C., Goldfarb, A., & Greenstein, S. (2012). The internet and local wages: A puzzle. *American Economic Review*, *102*(1), 556–575.
Forman, C., Goldfarb, A., & Greenstein, S. (2016). Agglomeration of invention in the bay area: Not just ICT. *American Economic Review*, *106*(5), 146–151.
Gambardella, A., Heaton, S., Novelli, E., & Teece, D. J. (2021). Profiting from enabling technologies? *Strategy Science*, *6*(1), 75–90.
Ganguli, I., Huysentruyt, M., & Le Coq, C. (2021). How do nascent social entrepreneurs respond to rewards? A field experiment on motivations in a grant competition. *Management Science*, *67*(10), 6294–6316.
Gans, J. S., Stern, S., & Wu, J. (2019). Foundations of entrepreneurial strategy. *Strategic Management Journal*, *40*(5), 736–756.
Ghemawat, P. (1991). *Commitment*. Simon and Schuster.
Goldfarb, A., Taska, B., & Teodoridis, F. (2023). Could machine learning be a general purpose technology? A comparison of emerging technologies using data from online job postings. *Research Policy*, *52*(1), 104653.
Goldfarb, A., & Trefler, D. (2019). Artificial intelligence and international trade. In A. Agrawal, J. Gans, & A. Goldfarb (eds.), *The economics of artificial intelligence: An agenda* (pp. 463–492). University of Chicago Press.

[Page 30]
Griliches, Z. (1957). Hybrid corn: An exploration in the economics of technological change. *Econometrica, Journal of the Econometric Society*, 25, 501–522.

Guzman, J. (2023). Go west young firm: The impact of startup migration on the performance of migrants. *Management Science*. Advance online publication.

Guzman, J., Oh, J. J., & Sen, A. (2020). What motivates innovative entrepreneurs? Evidence from a global field experiment. *Management Science*, 66(10), 4808–4819.

Guzman, J., & Stern, S. (2015). Where is silicon valley? *Science*, 347(6222), 606–609.

Guzman, J., & Stern, S. (2016). Nowcasting and placecasting entrepreneurial quality and performance. In *Measuring entrepreneurial businesses: Current knowledge and challenges* (pp. 63–109). University of Chicago Press.

Guzman, J., & Stern, S. (2020). The state of American entrepreneurship: New estimates of the quantity and quality of entrepreneurship for 32 US states, 1988–2014. *American Economic Journal: Economic Policy*, 12(4), 212–243.

Haltiwanger, J., Jarmin, R. S., & Miranda, J. (2013). Who creates jobs? Small versus large versus young. *Review of Economics and Statistics*, 95(2), 347–361.

Hoffreumon, C., Forman, C., & van Zeebroeck, N. (2023). *Make or buy your artificial intelligence? Testing for complementarities in technology sourcing* [Cornell University Working Paper].

Hurst, E., & Pugsley, B. W. (2011). What do small businesses do? *Brookings Papers on Economic Activity*, 42(2), 73–142.

Ichniowski, C., Shaw, K. L., & Prennushi, G. (1997). The effects of human resource management practices on productivity. *American Economic Review*, 86 (June 1997), 291–313.

Jaffe, A. B., Trajtenberg, M., & Henderson, R. (1993). Geographic localization of knowledge spillovers as evidenced by patent citations. *The Quarterly Journal of Economics*, 108(3), 577–598.

Jin, W., & McElheran, K. (2017). *Economies before scale: Survival and performance of young plants in the age of cloud computing* [Rotman School of Management Working Paper, 3112901].

Kapoor, R., & Teece, D. J. (2021). Three faces of technology's value creation: Emerging, enabling, embedding. *Strategy Science*, 6(1), 1–4.

Kazakova, S. S., Dunne, A. A., Bijwaard, D. D., Gossé, J., Hoffreumon, C., & van Zeebroeck, N. (2020). *European enterprise survey on the use of technologies based on artificial intelligence* (Technical Report). ULB Institutional Repository, ULB—Universite Libre de Bruxelles. https://EconPapers.repec.org/RePEc:ulb:ulbeco:2013/341443

Kerr, W. R., & Robert-Nicoud, F. (2020). Tech clusters. *Journal of Economic Perspectives*, 34(3), 50–76.

Lafontaine, F., & Shaw, K. (2016). Serial entrepreneurship: Learning by doing? *Journal of Labor Economics*, 34(S2), 217–254.

Lerner, J., & Nanda, R. (2020). Venture capital's role in financing innovation: What we know and how much we still need to learn. *Journal of Economic Perspectives*, 34(3), 237–261.

Levine, R., & Rubinstein, Y. (2018). *Selection into entrepreneurship and self-employment* (Technical Report). National Bureau of Economic Research.

Li, J. F. (2023). *Jump starting the AI engine: The complementary role of data and management practices*. Available at SSRN 4495624.

Lu, Y., Phillips, G. M., & Yang, J. (2023). *The impact of cloud computing and AI on industry dynamics and competition*. Available at SSRN 4480570.

McElheran, K. (2015). Do market leaders lead in business process innovation? The case (s) of e-business adoption. *Management Science*, 61(6), 1197–1216.

McElheran, K. (2018). *Economic measurement of AI* (Technical Report). National Bureau of Economic Research.

McElheran, K., & Jin, W. (2020). *Digital strategy in the age of cloud computing* [University of Toronto Working Paper, available at SSRN 4660979].

McElheran, K., Ohlmacher, S., & Yang, M. J. (2019). *Strategy and structured management*. Available at SSRN 4660979.

Miric, M., Jia, N., & Huang, K. G. (2023). Using supervised machine learning for large-scale classification in management research: The case for identifying artificial intelligence patents. *Strategic Management Journal*, 44(2), 491–519.

Muro, M., & Liu, S. (2021). *The geography of AI, which cities will drive the artificial intelligence revolution?* Brookings Institution.

Nanda, R., & Sørensen, J. B. (2010). Workplace peers and entrepreneurship. *Management Science*, 56(7), 1116–1126.

Porter, M. E. (1980). *Competitive strategy: Techniques for analyzing industries and competitors*. Free Press.

PwC. (2019). *2019 AI predictions*.

Raj, M., & Seamans, R. (2019). Primer on artificial intelligence and robotics. *Journal of Organization Design*, 8, 1–14.

Rosenberg, N. (1963). Technological change in the machine tool industry, 1840-1910. *The Journal of Economic History*, 23(4), 414–443.

Samila, S., & Sorenson, O. (2011). Venture capital, entrepreneurship, and economic growth. *The Review of Economics and Statistics*, 93(1), 338–349.

Shah, S. K., Agarwal, R., & Echambadi, R. (2019). Jewels in the crown: Exploring the motivations and team building processes of employee entrepreneurs. *Strategic Management Journal*, 40(9), 1417–1452.

Spulber, D. F. (2011a). How entrepreneurs affect the rate and direction of inventive activity. In J. Lerner & S. Stern (eds.), *The Rate and Direction of Inventive Activity Revisited* (pp. 277–315). University of Chicago Press.

Spulber, D. F. (2011b). Should business method inventions be patentable? *Journal of Legal Analysis*, 3(1), 265–340.

Tambe, P. (2014). Big data investment, skills, and firm value. *Management Science*, 60(6), 1452–1469.

Tambe, P., Hitt, L., Rock, D., & Brynjolfsson, E. (2020). *Digital capital and superstar firms* (Technical Report). National Bureau of Economic Research w28285.

[Page 31]
MCELHERAN ET AL.
405

Tambe, P., Hitt, L. M., & Brynjolfsson, E. (2012). The extroverted firm: How external information practices affect innovation and productivity. *Management Science, 58*(5), 843–859.

Trajtenberg, M. (2018). *AI as the next GPT: A political-economy perspective* (Technical Report). National Bureau of Economic Research.

Webb, M. (2019). The impact of artificial intelligence on the labor market. Available at SSRN 3482150.

Wu, L., Hitt, L., & Lou, B. (2020). Data analytics, innovation, and firm productivity. *Management Science, 66*(5), 2017–2039.

Wu, L., Lou, B., & Hitt, L. (2019). Data analytics supports decentralized innovation. *Management Science, 65*(10), 4863–4877.

Zolas, N., Kroff, Z., Brynjolfsson, E., McElheran, K., Beede, D. N., Buffington, C., Goldschlag, N., Foster, L., & Dinlersoz, E. (2020). *Advanced technologies adoption and use by U.S. firms: Evidence from the annual business survey* [NBER Working Papers 28290]. National Bureau of Economic Research Inc.

> **How to cite this article:** McElheran, K., Li, J. F., Brynjolfsson, E., Kroff, Z., Dinlersoz, E., Foster, L., & Zolas, N. (2024). AI adoption in America: Who, what, and where. *Journal of Economics & Management Strategy, 33*, 375–415. https://doi.org/10.1111/jems.12576

***

## APPENDIX A: APPENDIX TABLES AND FIGURES

### A.1 | Appendix tables
See Tables A1–A4.

### A.2 | Appendix figures
See Figures A1–A4.

***

**TABLE A1** Firm characteristics nonmanufacturing industries for specific AI technologies.

**Automated-guided vehicles (AGV)**

| NAICS | NAICS description | Mean (all industries) |
| :--- | :--- | :--- |
| | | 0.008 |
| 1151 | Support activities for crop production | 0.074 |
| 4245 | Farm product raw material merchant wholesalers | 0.048 |
| 2379 | Other heavy and civil engineering construction | 0.037 |

**Machine learning**

| NAICS | NAICS description | Mean (all industries) |
| :--- | :--- | :--- |
| | | 0.029 |
| 5112 | Software publishers | 0.103 |
| 5182 | Data processing, hosting, and related services | 0.084 |
| 5415 | Computer systems design and related services | 0.082 |

**Machine vision**

| NAICS | NAICS description | Mean (all industries) |
| :--- | :--- | :--- |
| | | 0.018 |
| 6115 | Technical and trade schools | 0.048 |
| 5112 | Software publishers | 0.041 |
| 5415 | Computer systems design and related services | 0.040 |

**Natural language processing**

| NAICS | NAICS description | Mean (all industries) |
| :--- | :--- | :--- |
| | | 0.013 |
| 5112 | Software publishers | 0.063 |
| 5191 | Other information services | 0.059 |
| 5415 | Computer systems design and related services | 0.056 |

(Continues)

[Page 32]
**TABLE A1** (Continued)

**Automated-guided vehicles (AGV)**

| NAICS | NAICS description | Mean (all industries) |
| :--- | :--- | :--- |
| | | 0.008 |

**Voice recognition**

| NAICS | NAICS description | Mean (all industries) |
| :--- | :--- | :--- |
| | | 0.026 |
| 6215 | Medical and diagnostic laboratories | 0.199 |
| 6211 | Offices of physicians | 0.159 |
| 5411 | Legal services | 0.093 |

Notes: Tabulated from the ABS-LBD linked sample (column 1, Table 1) Shares are computed using the LBD tabulation weights of firm counts, divided by the total number of firms (including those that responded with "Don't Know" or missing). The shares are then scaled up by the total number of nonmissing and "Don't Know" responses for each technology. The 2017 industry figures from the LBD are the figures listed in the tables. Industry tabulations for multiunit firms are generated from the largest payroll industry within the firm (if there is a tie, then the industry with the most employment is used).
Abbreviations: ABS, Annual Business Survey; AI, artificial intelligence; LBD, Longitudinal Business Database; NAICS, North American Industry Classification System.

**TABLE A2** Large CBSAs by AI usage rate among single-unit startups.

| | **(1) Firm-weighted** | | **(2) Employment-weighted** | |
| :--- | :--- | :--- | :--- | :--- |
| **CBSA** | **Share** | **Rank** | **Share** | **Rank** |
| Atlanta-Sandy Springs-Roswell, GA | 6.1 | 18 | 12.2 | 7 |
| Austin-Round Rock, TX | 5.4 | 33 | 15 | 5 |
| Baltimore-Columbia-Towson, MD | 3 | 49 | 6.3 | 28 |
| Boston-Cambridge-Newton, MA-NH | 6.7 | 13 | 7.6 | 19 |
| Charlotte-Concord-Gastonia, NC-SC | 5.6 | 29 | 7 | 23 |
| Chicago-Naperville-Elgin, IL-IN-WI | 5.4 | 33 | 10.3 | 9 |
| Cincinnati, OH-KY-IN | 5 | 39 | 5.4 | 33 |
| Cleveland-Elyria, OH | 4.5 | 40 | 6.9 | 25 |
| Columbus, OH | 4.5 | 40 | 16.1 | 4 |
| Dallas-Fort Worth-Arlington, TX | 6.8 | 10 | 6 | 30 |
| Denver-Aurora-Lakewood, CO | 4.5 | 40 | 2.4 | 48 |
| Detroit-Warren-Dearborn, MI | 5.7 | 25 | 8.1 | 16 |
| Hartford-West Hartford-East Hartford, CT | 6.8 | 10 | 2.5 | 47 |
| Houston-The Woodlands-Sugar Land, TX | 6.2 | 17 | 8.2 | 15 |
| Indianapolis-Carmel-Anderson, IN | 3.8 | 45 | 2.9 | 45 |
| Jacksonville, FL | 4.5 | 40 | 3.3 | 41 |
| Kansas City, MO-KS | 6.6 | 15 | 6.1 | 29 |
| Las Vegas-Henderson-Paradise, NV | 7.7 | 4 | 3.2 | 43 |
| Los Angeles-Long Beach-Anaheim, CA | 5.8 | 23 | 9.4 | 10 |
| Louisville/Jefferson County, KY-IN | 5.6 | 29 | 18.8 | 3 |
| Miami-Fort Lauderdale-West Palm Beach, FL | 5.8 | 23 | 4.2 | 36 |
| Milwaukee-Waukesha-West Allis, WI | 4.2 | 44 | 8.3 | 14 |

[Page 33]
MCELHERAN ET AL.
407

Journal of Economics & Management Strategy
WILEY

**TABLE A2** (Continued)

| | **(1) Firm-weighted** | **(2) Employment-weighted** |
| :--- | :---: | :---: | :---: | :---: |
| **CBSA** | **Share** | **Rank** | **Share** | **Rank** |
| Minneapolis-St. Paul-Bloomington, MN-WI | 5.7 | 25 | 7 | 23 |
| Nashville-Davidson-Murfreesboro-Franklin, TN | 8.3 | 2 | 11.8 | 8 |
| New Orleans-Metairie, LA | 7.4 | 5 | 4 | 37 |
| New York-Newark-Jersey City, NY-NJ-PA | 5.5 | 32 | 8.6 | 13 |
| Oklahoma City, OK | 3.8 | 45 | 5.8 | 31 |
| Orlando-Kissimmee-Sanford, FL | 5.1 | 37 | 2.3 | 49 |
| Philadelphia-Camden-Wilmington, PA-NJ-DE-MD | 6 | 19 | 7.5 | 20 |
| Phoenix-Mesa-Scottsdale, AZ | 5.9 | 21 | 7.8 | 17 |
| Pittsburgh, PA | 5.1 | 37 | 7.8 | 17 |
| Portland-Vancouver-Hillsboro, OR-WA | 5.4 | 33 | 6.9 | 25 |
| Providence-Warwick, RI-MA | 3.8 | 45 | 3.8 | 38 |
| Raleigh, NC | 6.9 | 9 | 3.3 | 41 |
| Richmond, VA | 5.6 | 29 | 4.3 | 35 |
| Riverside-San Bernardino-Ontario, CA | 5.9 | 21 | 20 | 1 |
| Sacramento-Roseville-Arden-Arcade, CA | 6.4 | 16 | 9.1 | 11 |
| St. Louis, MO-IL | 5.7 | 25 | 3.6 | 40 |
| Salt Lake City, UT | 5.7 | 25 | 5.7 | 32 |
| San Antonio-New Braunfels, TX | 8.3 | 2 | 3.8 | 38 |
| San Diego-Carlsbad, CA | 7.4 | 5 | 5.1 | 34 |
| San Francisco-Oakland-Hayward, CA | 9.5 | 1 | 18.9 | 2 |
| San Jose-Sunnyvale-Santa Clara, CA | 7.1 | 8 | 13.6 | 6 |
| Seattle-Tacoma-Bellevue, WA | 6.8 | 10 | 8.7 | 12 |
| Tampa-St. Petersburg-Clearwater, FL | 7.4 | 5 | 7.4 | 21 |
| Tucson, AZ | 6.7 | 13 | 6.4 | 27 |
| Tulsa, OK | 6 | 19 | 3.2 | 43 |
| Virginia Beach-Norfolk-Newport News, VA-NC | 3.6 | 48 | 2.6 | 46 |
| Washington-Arlington-Alexandria, DC-VA-MD-WV | 5.2 | 36 | 7.4 | 21 |
| **Mean micropolitan (<50,000 persons)** | **4.1** | – | **8.2** | – |
| **Mean small-sized CBSA (50,000-250,000 persons)** | **4.9** | – | **6.7** | – |
| **Mean medium-sized CBSA (250,000-1,000,000 persons)** | **4.5** | – | **6.8** | – |
| **Mean large-sized CBSA (>1,000,000 persons)** | **5.9** | – | **7.7** | – |

*Notes*: This table reports the AI usage rates among single-unit startups in large CBSAs. Large CBSAs are those with more than 1,000,000 persons. Usage rates are computed using a modified firm weight based on the national share of single-units within strata defined by size class, age class, and two-digit NAICS sector. Unlike our "startup sample" described in Table 1 (and used for regressions in Tables 6a, 6b, and 7), the underlying sample of this table is not restricted to firms with owner or revenue information. Rather, the underlying sample is a subset of our baseline sample—specifically, single-unit startups located in large CBSAs (roughly 30,000 firms). For comparison, the final four rows (bolded) report mean usage rates for each CBSA size classification.

*Abbreviations*: AI, artificial intelligence; CBSA, core-based statistical area; NAICS, North American Industry Classification System.

[Page 34]
TABLE A3 AI usage rates by firm characteristics (%) startup sample.

| | **AI usage rate (%)** | | |
|:---|:---:|:---:|:---:|
| | **Yes** | **No** | **Difference** |
| **Full sample** | **6.0** | | |
| **A. Primary owner characteristics** | | | |
| Hold advanced degree | 8.4 | 5.3 | 3.1 |
| Owned prior business | 6.4 | 5.8 | 0.6 |
| Missing age | 7.7 | 5.9 | 1.8 |
| Owner age (0-34) | 5.9 | 6 | -0.1 |
| Owner age (35-54) | 6.1 | 5.9 | 0.2 |
| Owner age (55+) | 5.6 | 6.2 | -0.6 |
| **"Very Important" reasons for owning the business** | | | |
| Wanted to be own boss | 5.9 | 6.2 | -0.3 |
| Flexible hours | 5.8 | 6.2 | -0.4 |
| Balance work and family | 5.9 | 6.2 | -0.3 |
| Opportunity for greater income | 6 | 6 | 0 |
| Best avenue for ideas/goods/services | 6.5 | 5.3 | 1.2 |
| Unable to find employment | 7.5 | 5.9 | 1.6 |
| Working for someone else not appealing | 6.2 | 5.9 | 0.3 |
| Always wanted to start own business | 6.1 | 5.9 | 0.2 |
| Entrepreneurial role model | 6.6 | 5.8 | 0.8 |
| Carry on family business | 6.9 | 5.9 | 1 |
| Help or become involved in community | 7.6 | 5.5 | 2.1 |
| Other reasons | 8 | 5.8 | 2.2 |
| Lifestyle reason | 5.9 | 6.1 | -0.2 |
| **B. Startup conditions** | | | |
| Funded by VC | 18.8 | 5.9 | 12.9 |
| Missing startup capitalization | 4.5 | 6.2 | -1.7 |
| Startup capitalization <25K | 6 | 6 | 0 |
| Startup capitalization 25K-1M | 6.6 | 5.6 | 1 |
| Startup capitalization 1M+ | 9.2 | 5.9 | 3.3 |
| Don't know startup capitalization | 5.3 | 6.1 | -0.8 |
| **C. Innovative strategies and outcomes** | | | |
| Process innovation | 11.9 | 4.6 | 7.3 |
| Product innovation | 7.4 | 4.4 | 3 |
| Patents owned or pending | 14.8 | 5.8 | 9 |
| IP is very important | 12.5 | 4.4 | 8.1 |
| Growth-oriented innovation strategy | 6.7 | 4.4 | 2.3 |
| **D. Geography** | | | |
| In micropolitan or rural CBSA (<50, 000) | 5.3 | 6.2 | -0.9 |
| In small-sized CBSA (<250, 000) | 5.3 | 6.1 | -0.8 |

[Page 35]
MCELHERAN ET AL.
409

**TABLE A3** (Continued)

| | **AI usage rate (%)** | | |
| :--- | :--- | :--- | :--- |
| | **Yes** | **No** | **Difference** |
| **Full sample** | 6.0 | | – |
| In medium-sized CBSA (<1, 000, 000) | 5.8 | 6.1 | −0.3 |
| In large-sized CBSA (1,000,000+) | 6.6 | 5.4 | 1.2 |

*Notes*: "Use" is defined as having responded with "In use for less than 5% of production or service," "In use for between 5%-25% of production or service," or "In use for more than 25% of production or service" for the category listed on any of the AI-based Business Technologies. The "Growth-oriented innovation strategy" indicator is equal to 1 if a firm responded that a focus on introducing new goods or services, reaching new customer groups, or opening up new domestic or export markets was a "very important" strategy for the business. The underlying sample for this table is our startup sample (column 4, Table 1).
*Abbreviations*: AI, artificial intelligence; CBSA, core-based statistical area; IP, intellectual property; VC, venture capital.

---

**TABLE A4** Correlates of AI adoption—including early and later firm growth rates owner and revenue sample.

| Description | (1)<br>Use AI | (2)<br>Use AI | (3)<br>Use AI | (4)<br>Use AI | (5)<br>Use AI |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Revenue growth (first 3 years)** | 0.0075***<br>(0.0016) | 0.0073***<br>(0.0016) | 0.0061***<br>(0.0016) | 0.0074***<br>(0.0016) | 0.0021<br>(0.0016) |
| **Revenue growth (last 3 years)** | 0.0093***<br>(0.0019) | 0.0088***<br>(0.0019) | 0.0083***<br>(0.0019) | 0.0093***<br>(0.0019) | 0.0041**<br>(0.0018) |
| **Advanced degree (1/0)** | | 0.0148***<br>(0.0019) | | | 0.0087***<br>(0.0018) |
| **Prior business (1/0)** | | 0.0102***<br>(0.0013) | | | 0.0050***<br>(0.0013) |
| **Owner age (35-54)** | | −0.0039<br>(0.0026) | | | 0.0004<br>(0.0026) |
| **Owner Age (55+)** | | −0.0082***<br>(0.0027) | | | −0.0014<br>(0.0027) |
| **Lifestyle reason (1/0)** | | 0.0012<br>(0.0013) | | | −0.0021<br>(0.0013) |
| **Funded by venture capital (1/0)** | | | 0.0770***<br>(0.0103) | | 0.0578***<br>(0.0101) |
| **Startup capitalization 25K-1M (1/0)** | | | 0.0159***<br>(0.0015) | | 0.0090***<br>(0.0015) |
| **Startup capitalization 1M+ (1/0)** | | | 0.0271***<br>(0.0044) | | 0.0130***<br>(0.0044) |
| **Process innovation (1/0)** | | | | | 0.0574***<br>(0.0020) |
| **Product innovation (1/0)** | | | | | 0.0090***<br>(0.0012) |
| **Patents owned or pending (1/0)** | | | | | 0.0329***<br>(0.0064) |
| **IP is very important (1/0)** | | | | | 0.0572***<br>(0.0021) |
| | | | | | (Continues) |

[Page 36]
TABLE A4 (Continued)
| Description | (1) Use AI | (2) Use AI | (3) Use AI | (4) Use AI | (5) Use AI |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Growth-oriented innovation strategy (1/0) | | | | | 0.0091*** |
| | | | | | (0.0012) |
| Small CBSA | | | | 0.0012 | 0.0003 |
| | | | | (0.0023) | (0.0022) |
| Medium CBSA | | | | 0.0017 | -0.0004 |
| | | | | (0.0019) | (0.0019) |
| Large CBSA | | | | 0.0046*** | 0.0013 |
| | | | | (0.0017) | (0.0017) |
| State-by-industry controls | Yes | Yes | Yes | Yes | Yes |
| Firm age controls | Yes | Yes | Yes | Yes | Yes |
| Owner gender controls | Yes | Yes | Yes | Yes | Yes |
| Observations (rounded) | 209,000 | 209,000 | 209,000 | 209,000 | 209,000 |
| R² | 0.125 | 0.126 | 0.127 | 0.125 | 0.148 |

Notes: Standard errors in parentheses. Revenue growth refers to the 3-year average of the log-difference measure of annual revenue growth. "Use" is defined as having responded with "In use for less than 5% of production or service," "In use for between 5%-25% of production or service," or "In use for more than 25% of production or service" for the category listed on any of the AI-based Business Technologies (Automated-Guided Vehicles, Natural Language Processing, Machine Learning, Machine Vision, and Voice Recognition). State-by-industry controls refer to state and six-digit NAICS industry dummies. The underlying sample for this table is our owner and revenue sample (column 3, Table 1). Note that column (5) is identical to column (7) of Table 7.
Abbreviations: AI, artificial intelligence; CBSA, core-based statistical area; IP, intellectual property; NAICS, North American Industry Classification System.
*, **, and *** denote significance at 10%, 5%, and 1%, respectively.

[CHART: A horizontal stacked bar chart titled 'AI and robotics use by firm size full ABS sample.' The y-axis lists firm sizes by number of employees, from '1-4 Employees' at the bottom to '10,000+ Employees' at the top. The x-axis represents percentages from 0% to 100%. Each bar shows the percentage of firms using 'AI Only' (light gray), 'AI & Robotics' (dark gray), or 'Robotics Only' (black). The chart shows that larger firms have a higher percentage of AI and/or robotics use, with the proportion of 'AI & Robotics' use increasing significantly with firm size.]

FIGURE A1 AI and robotics use by firm size full ABS sample. Notes: This figure reports the percentage of firms that use AI or robotics among firms in the ABS-LBD linked sample (column 1, Table 1) that reported using either an AI-based technology or robotics (roughly 34, 000 firms). AI use is defined by the weighted share of firms by sector that indicate intensity of use of at least 1 of the following business technologies: Automated-Guided Vehicles, Machine Learning, Machine Vision, Natural Language Processing, and Voice Recognition. Robotics use is collected from the same survey question (see Table 2) and similarly weighted. ABS, Annual Business Survey; AI, artificial intelligence; LBD, Longitudinal Business Database.

[Page 37]
MCELHERAN ET AL.
Journal of Economics & Management Strategy WILEY
411

[CHART: A map of the United States showing AI use rates by young single-unit firms across large core-based statistical areas (CBSAs). Bubbles are located over various cities, with their size and color corresponding to the legend.]

**AI Percentile**
100
75
50
25
0

**AI Firms (Emp Weighted)**
1000
2000
3000

FIGURE A2 AI use rates by Young single-unit firms across large core-based statistical areas (CBSAs)—Employment-weighted. Notes: The map includes the largest (population >1,000,000) CBSAs. Bubble sizes in the map represent the employment-weighted number of single-unit startups (i.e., firm age ≤5 years) that use AI within each CBSA, and the color gradient represents the percentile rank of the usage rate of AI across single-unit startups within the largest CBSAs. Unlike our “startup sample” described in Table 1 (and used for regressions in Tables 6a, 6b, and 7), the underlying sample of this figure is not restricted to firms with owner or revenue information. Rather, the underlying sample is a subset of our baseline sample—specifically, single-unit startups located in large CBSAs (roughly 30,000 firms). AI, artificial intelligence; CBSA, core-based statistical area.

[Page 38]
(a)

[CHART: A map of the United States showing data points as colored and sized circles in various Core-Based Statistical Areas (CBSAs). The legend on the right indicates that the color represents the "AI Percentile" with a gradient from yellow (0), green (25), cyan (50), blue (75), to dark purple (100). The size of the circle represents the "Number of AI Firms," with a medium circle for 5000 and a large circle for 10000.]

(b)

[CHART: A second map of the United States, similar to the first, with data points as colored and sized circles. The legend on the right indicates that the size of the circle represents the "Number of AI Firms," with a small circle for 10000, a medium circle for 20000, and a large circle for 30000. The color represents the "AI Percentile" with a gradient from yellow (0), green (25), cyan (50), blue (75), to dark purple (100).]

FIGURE A3 (a) AI use rates by single-unit firms across CBSAs. *Notes:* The map includes the 350 CBSAs with at least 20 single-unit firms using AI. Bubble sizes in the map represent the (firm-weighted) number of single-unit firms from our baseline sample that use AI within each CBSA, and the color gradient represents the percentile rank of the adoption rate of AI across single-unit firms within each CBSA type: Micropolitan (<50, 000 persons), Small (50,000-250,000 persons), Medium Small (250,000-1,000,000 persons), and Large (>1, 000, 000 persons). (b) AI use rates by single-unit firms across CBSAs-Employment-weighted. *Notes:* The map includes the 350 CBSAs with at least 20 single-unit firms using AI. Bubble sizes in the map represent the employment-weighted number of single-unit firms from our baseline sample that use AI within each CBSA, and the color gradient represents the percentile rank of the adoption rate of AI across single-unit firms within each CBSA type: Micropolitan (<50, 000 persons), Small (50,000-250,000 persons), Medium Small (250,000-1,000,000 persons), and Large (>1, 000, 000 persons). AI, artificial intelligence; CBSA, core-based statistical area.

[Page 39]
MCELHERAN ET AL.
Journal of Economics & Management Strategy
WILEY-
413

[CHART: A Sankey diagram illustrating the flow of firms through different stages of technology adoption. On the far left, a single gray bar represents "ABS Technology Users". From this bar, three gray flows emerge, splitting into three categories in the center. The top flow, colored light gray, goes to a box labeled "Low Digitization" and "Low Cloud Computing". The middle flow, colored orange, is the thickest and goes to a box labeled "Medium Digitization" and "Medium Cloud Computing". The bottom flow, also colored orange, goes to a box labeled "High Cloud Computing" and "High Digitzation". All three of these flows then converge into a single green bar on the far right labeled "AI Adoption". The width of the gray areas represents the number of firms at each stage.]

**FIGURE A4** Technological interdependencies by intensity. Notes: Sankey representation of firm counts in the ABS-LBD linked sample (column 1, Table 1) as they progress from no technology adoption to reliance on digital information, then cloud computing, and finally AI adoption. The size of the gray area is representative of the number of firm progressing to the next "stage" of technology use. Note that the calculations are made using imputed values for missing responses. Use of AI constitutes the weighted count of firms that indicate use intensity of at least 1 of the following business technologies: Automated-Guided Vehicles, Machine Learning, Machine Vision, Natural Language Processing, and Voice Recognition (Table 2). Low, Medium, and High intensity use of Digitization and Cloud Computing refer to the respondent answering "All" (corresponds to "High"), "More than 50%" (corresponds to "Medium"), and "Less than 50%" corresponds to "Low" for at least one Digital Share of Business Activity or Cloud Service Purchases. ABS, Annual Business Survey; AI, artificial intelligence; LBD, Longitudinal Business Database.

15309134, 2024, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/jems.12576, Wiley Online Library on [10/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

[Page 40]
# APPENDIX B: DATA APPENDIX

## B.1 | Overview of the ABS
The ABS was first conducted in 2018 in partnership between the Census Bureau and the NCSES within the National Science Foundation. It covers all nonfarm employer businesses filing the IRS 941, 944, or 1120 tax forms (which includes publicly traded firms). Firms surveyed are selected based on a sampling method that stratifies firms by state, industry, and ownership ethnicity and gender (for details on the 2018 ABS sampling methodology, visit https://www. census.gov/programs-surveys/abs/technical-documentation/methodology.2018.html).

The ABS consolidates three earlier data collections: the Survey of Business Owners (SBOs), the Annual Survey of Entrepreneurs (ASEs), and the Business R&D and Innovation Survey for Microbusinesses (BRDI-Ms). The SBO was conducted by the Census Bureau; the ASE was conducted by the Census Bureau in partnership with the Ewing Marion Kauffman Foundation and the Minority Business Development Agency; and the BRDI-M was conducted by the Census Bureau under a partnership with NCSES. The ABS also includes an innovation section—in part derived from the 2016 Business R&D and Innovation Survey-to provide an expanded set of nationally representative business innovation statistics As a result of these consolidations from earlier collections, the ABS captures many important features of US businesses, including ownership and owner characteristics, startup or acquisition funding, initial capitalization and firm financing, IP strategy, and several aspects of innovation and R&D. The only purpose-designed questions for this inaugural wave of the ABS pertained to digitization, cloud computing, and advanced business technology use, as described in Section 3. See Zolas et al. (2020) for additional details on this technology module, and see https://www. census.gov/programs-surveys/abs/about.html for more details about the ABS overall.

## B.2 | Measuring owner characteristics, startup financing, and firm innovation and business strategies in the ABS
### B.2.1 | Education
The ABS asks "Prior to establishing, purchasing, or acquiring this business, what was the highest degree or level of school" the owner completed? There are nine checkbox responses ranging from “Less than high school/secondary school graduate” to “Professional Degree, beyond a Bachelor's Degree (e.g., MD, DDS, DVM, LLB, JD)." We construct an indicator of having an advanced degree, defined as having a master's, doctoral, or professional degree.

### B.2.2 | Serial entrepreneurship
The ABS asks, “Prior to establishing, purchasing, or acquiring this business, how many previous businesses has the owner owned?" Six possible responses range from 0 to 5 or more, though the important variation is captured by an indicator for any prior ownership.

### B.2.3 | Owner age
Six checkboxes solicit owner age: under 25, 25–34, 35–44, 45–54, 55–64, and 65 or over. We collapse this into three informative categories: less than 35 (omitted group), 35-54, and 55+ years.

### B.2.4 | Owner aspirations
The ABS asks about how important (very important, somewhat important, and not at all important) are 12 potential reasons for owning this business. These reasons include: "Wanted to be my own boss,” “Flexible hours,” “Balance work and family," "Opportunity for greater income,” “Best avenue for my ideas/goods/services,” “Unable to find employment," "Working for someone else didn't appeal to me," "Always wanted to start my own business,” “An entrepreneurial friend or family member was my role model,” “Wanted to carry on the family business," wanted to "Help and/or become more involved in my community," and "Other (Specify)." We construct an indicator which receives a value of 1 if the primary owner reports either "flexible hours” or “balance work and family" as a “very important" reason for owning the business.

### B.2.5 | Funding sources
For sources of capital, there are 12 checkbox options provided and respondents can check all that apply. Options include personal/family sources (separately for savings, other assets, home equity loans, and credit cards), business credit cards, business loans (separately for government-guaranteed, bank or financial institution, and government), investment (separately for from family/friends and VC), grants, and other sources.

[Page 41]
**B.2.6 | Funding levels**
Regarding the total amount of capital, 10 checkboxes range from less than 5000 dollars to 3 million dollars or more,
including a “Don't Know” option: less than $5000; $5000–$9999; $10,000–$24,999; $25,000–$49,999; $50,000–$99,999;
$100,000–$249,999; $250,000–$999,999; $1,000,000–$2,999,999; and $3,000,000 or more. We collapse these ranges into
three broader ranges: less than $25,000; $25,000–$999,999; and $1,000,000 or more.

**B.2.7 | Innovation**
The ABS asks about process and product innovation, separately, across the prior 3 years (2015–2017). The process
innovation question asks whether the business introduced new or significantly improved manufacturing methods;
logistics, delivery, or distribution methods; and supporting activities for such processes (such as maintenance systems
or operations for purchasing, accounting or computing). The product innovation question asks whether the business
introduced new or significantly improved goods or services. Response options to both are “yes,” “no,” and “not
applicable.” We construct indicators for each.

To measure the firm's reliance on formal IP, we first combine two questions that capture the number of US patent
applications pending and the number of US patents owned by the business by the end of 2017, collapsing them into an
indicator of any patents owned or pending.

We also leverage questions on the ABS about the level of importance (very important, somewhat important, and not
at all important) of the following six types of IP protection: utility patents (patents for inventions), design patents
(patents for appearance), trademarks, copyrights, trade secrets, and nondisclosure agreements.

**B.2.8 | Business strategy**
In the section on Innovation, the ABS elicits the importance (very important, somewhat important, and not at all
important) of 14 business strategies over 2015–2017. These strategies include: improving existing goods/services,
introducing new goods/services, reaching new customer groups, customer-specific solutions, lowering price, reducing
costs, satisfying key customers, developing niche/specialized markets, opening up new domestic markets, opening up
new export markets, improving internal processes, improving delivery of existing goods/services, improving workforce,
and understanding/meeting customer needs. We consider a business as having a “growth-oriented” strategy if it
reported that introducing new goods or services, reaching new customer groups, or opening up new domestic or export
markets were “very important.”

**B.3 | Tabulation weights for geographic results**
Because the samples for Figures 5, A2, A3a,b, and Table A2 contain only single-unit firms, these differ somewhat from
our nationally representative baseline sample described in Section 3.1. We thus modify our firm weights. Instead of
generating weights based on the universe of firms in the LBD, we generate weights to represent the universe of single-
unit firms in the LBD. The stratification we use for calculating the new weights does not explicitly include geographic
information. A more complete dive into the geography of AI diffusion would likely benefit from a more nuanced
weighting scheme that directly incorporates geographic information in some manner. Regarding the method of
generating weights, our nonparametric weighting scheme ensures that the weighted number of surveyed ABS firms is
equal to the number of firms in the same respective strata in the LBD. But this relies on a critical mass of surveyed
firms in each stratum to avoid assigning unusually large values as weights, and including geography as an additional
stratum would result in very small cells. We thus recommend a parametric weighting approach for researchers aiming
to incorporate geography directly into the design of firm weights.