

[Page 1]
# Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence

Erik Brynjolfsson*
Bharat Chandar†
Ruyu Chen‡§

November 13, 2025

*Abstract*

Using high-frequency administrative data from ADP, we document six facts characterizing labor market shifts following the widespread adoption of generative AI. Early-career workers (ages 22-25) in AI-exposed occupations experienced 16% relative employment declines, controlling for firm-level shocks, while employment for experienced workers remained stable. Adjustments occur primarily via employment rather than compensation, with employment changes concentrated in occupations where AI automates rather than augments labor. Results are robust to excluding technology firms and occupations that are remotable. These six facts provide early large-scale evidence consistent with generative AI disproportionately impacting entry-level workers in the American labor market.

***

*Stanford University and NBER; erikb@stanford.edu
†Stanford University; chandarb@stanford.edu
‡Stanford University; ruyuchen@stanford.edu
§We thank to David Autor, Sarah Bana, Eric Bergman, Nick Bloom, Cody Cook, Chris Forman, Joshua Gans, Basil Halperin, Christina Langer, Fei-Fei Li, Frank Li, Omeed Maghzian, Jiaxin Pei, Daniel Rock, Brad Ross, Phil Trammell, Andrew Wang, and participants at the Stanford Digital Economy Lab workshop for helpful feedback. We are grateful to ADP for access to the data and the Stanford Digital Economy Lab for financial support. All errors are our own.
¶Latest version: https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/

[Page 2]
# 1 Introduction
The proliferation of generative artificial intelligence (AI) has sparked a global debate about its
potential impact on the labor market. This discourse spans utopian predictions of enhanced pro-
ductivity, dystopian fears of widespread job displacement, and skeptical views that AI will have
minimal effects on employment or productivity. Historically, technologies have affected different
tasks, occupations, and industries in different ways, replacing work in some, augmenting others,
and transforming still others. These heterogeneous effects suggest that there may be "canaries in
the coal mine" which are harbingers of more widespread effects of AI.

Recent discussion coincides with rapid improvements in AI capabilities and adoption. From
2023 to 2024, AI systems improved from solving 4.4% of coding problems to 71.7% on SWE-Bench,
a widely used benchmark for software engineering (Maslej et al., 2025). AI has also improved in
areas like language understanding, subject knowledge, and reasoning. A recent paper found that
current systems could match or outperform up to 47 percent of industry professionals on a pre-
defined benchmark of economically valuable tasks (Patwardhan et al., 2025). At the same time,
AI systems are increasingly widely adopted. Hartley et al. (2025) find that LLM adoption at work
among U.S. survey respondents above age 18 reached 46% by June/July 2025.¹

Given the better capabilities and widespread adoption, a central concern, amplified in recent
headlines, is whether AI is beginning to supplant human labor, particularly for younger, entry-level
workers in highly exposed professions like software engineering and customer service.² For instance,
in May of 2025, Dario Amodei, co-founder and CEO of Anthropic predicted that AI could wipe
out roughly 50 percent of all entry-level white-collar jobs within five years (Morris, 2025).

Despite the intensity of this debate, empirical evidence has struggled to keep pace with techno-
logical advancement, leaving many fundamental questions unanswered. This paper confronts this
empirical gap by leveraging a large-scale, high-frequency administrative dataset from ADP, the
largest payroll software provider in the United States. Our sample consists of monthly, individual-
level payroll records through September 2025, encompassing millions of workers across tens of
thousands of firms. This rich panel structure allows us to track employment dynamics with a high

---
¹Similarly, Bick et al. (2024) found that in late 2024, nearly 40% of the U.S. population age 18-64 reported using
generative AI, with 23% using it for work weekly and 9% daily.
²Improved productivity of workers in an occupation could lead to either reduced or increased employment, de-
pending on, among other things, how elastic demand is for the output of those workers.

[Page 3]
degree of granularity, providing a near real-time view of labor market adjustments. By linking this
data to established measures of occupational AI exposure and other variables, we can quantify the
realized employment changes since the widespread adoption of generative AI.

This paper systematically presents six key facts that emerge from the data, offering an assess-
ment of how the AI revolution is reshaping the American workforce.

Our first key finding is that we uncover substantial declines in employment for early-career
workers (ages 22-25) in occupations most exposed to AI, such as software developers and cus-
tomer service representatives. In contrast, employment trends for more experienced workers in the
same occupations, and workers of all ages in less-exposed occupations such as nursing aides, have
remained stable or continued to grow.

Our second key fact is that overall employment continues to grow robustly, but employment
growth for young workers has been stagnant since late 2022. In jobs less exposed to AI, young
workers have experienced comparable employment growth to older workers. In contrast, workers
aged 22 to 25 have experienced a 6% decline in employment from late 2022 to September 2025 in
the most AI-exposed occupations, compared to a 6-9% increase for older workers. These results
suggest that declining employment in AI-exposed jobs drives stagnant overall employment growth
for 22- to 25-year-olds.

Our third key fact is that not all uses of AI are associated with declines in employment. In
particular, entry-level employment has declined in applications of AI that *automate* work, but not
those that most *augment* it. We distinguish between automation and augmentation empirically us-
ing estimates of the extent to which observed queries to Claude, the LLM, substitute or complement
the tasks in that occupation. While we find employment declines for young workers in occupations
where AI primarily automates work, we find employment *growth* in occupations in which AI use
is most augmentative. These findings are consistent with automative uses of AI substituting for
labor while augmentative uses do not.

Fourth, we find that employment declines for young, AI-exposed workers remain after condition-
ing on firm-time effects. One class of explanations for our patterns is that they may be driven by
industry- or firm-level shocks such as interest rate changes that correlate with sorting patterns by
age and measured AI exposure. We test for a class of such confounders by controlling for firm-time
effects in an event study regression, absorbing aggregate firm shocks that impact all workers at a

[Page 4]
firm regardless of AI exposure. For workers aged 22-25, we find a 15 log-point decline in relative
employment for the most AI-exposed quintiles compared to the least exposed quintile, a large and
statistically significant effect. Estimates for other age groups are much smaller in magnitude and
not statistically significant. These findings imply that the employment trends we observe are not
driven by differential shocks to firms that employ a disproportionate share of AI-exposed young
workers.

Fifth, the labor market adjustments are visible in employment more than in compensation.
In contrast to our findings for employment, we find little difference in annual salary trends by
age or exposure quintile, suggesting possible wage stickiness. If so, AI may have larger effects on
employment than on wages, at least initially, or even that AI may boost wages for as many workers
as it hurts.

Sixth, the above facts are largely consistent across sample constructions designed to address
various alternative explanations for the core findings. Our results are not driven solely by computer
occupations or by occupations susceptible to remote work and outsourcing. We also find that the AI
exposure taxonomy did not meaningfully predict employment outcomes for young workers further
back in time, before the widespread use of LLMs, including during the unemployment spike driven
by the COVID-19 pandemic. The patterns we observe in the data appear most acutely starting
in late 2022 and early 2023, around the time of rapid proliferation of generative AI tools.³ They
hold for both occupations with a high share of college graduates and ones with a low college
share, suggesting deteriorating education outcomes during COVID-19 do not drive our results. For
non-college workers, we find evidence that experience may serve as less of a buffer to labor market
disruption, as low college share occupations exhibit divergent employment outcomes by AI exposure
up to age 40.

While we explore a variety of alternative explanations, we caution that the facts we document
may in part be influenced by factors other than generative AI. Taken as a whole, our results are
consistent with the hypothesis that generative AI has begun to affect entry-level employment. We
intend to continue to track the data on an ongoing basis to assess whether these trends change in
the future.

³In particular, OpenAI introduced ChatGPT in November 2022. It was reported to have over 100 million active
users by January 2023 and 1.7 billion website visitors in October 2023 (DeVon, 2023).

[Page 5]
Why might AI adversely affect exposed entry-level workers more than other age groups? One
possibility is that AI disproportionately substitutes for workers using codified knowledge, includ-
ing both the “book-learning” that forms the core of formal education and the insights in digital
company data that can be codified by AI. AI may be less capable of replacing tacit knowledge,
the idiosyncratic tips and tricks that accumulate with experience but which are never digitized.⁴
As young workers supply relatively more codified knowledge than tacit knowledge, they may face
greater task replacement from AI in exposed occupations, leading to greater employment realloca-
tion (Acemoglu and Autor, 2011). Older workers with accumulated tacit knowledge may face less
task replacement. These benefits of uncodified knowledge may accrue less to non-college workers
in occupations with low returns to experience. In other words, AI may be automating the *cod-
ifiable, checkable* tasks that historically justified entry-level headcount, while complementing the
judgment-, client-, and process-intensive tasks performed by experienced workers.

Other explanations may contribute. AI may raise the leverage of experienced staff, increasing
their effective span of control (Ide, 2025). Reduced hiring may also be the lowest-friction adjustment
margin, compounded by inefficient incentives to train entry-level workers who may move firms
(Becker, 1994; Garicano, 2025; Garicano and Rayo, 2025). Consequently firms may primarily
shrink junior inflows rather than displace incumbents.

This combination of task substitution at the apprentice margin, complementarity at the expert
margin, and quantity (not price) adjustment under wage ladders can explain why early-career
employment falls while employment of older workers continues to grow. An important direction for
research is to further model and test these predictions.

## 2 Related Literature

A growing body of research has sought to measure the employment effects of AI.⁵ This includes
influential papers that established methodologies for estimating which occupations and tasks were
susceptible to automation (Frey and Osborne, 2017; Brynjolfsson and Mitchell, 2017; Brynjolfsson
et al., 2018; Felten et al., 2018, 2019; Webb, 2019; Felten et al., 2021). More recently, work such

---
⁴Ironically, one of the practical skills more likely to be learned on the job than in university computer science
classes may be how to use AI for software development.
⁵There has also been extensive media discusssion of this topic including Thompson (2025); Raman (2025); Roose
(2025); The Economist (2025); Frick (2025). See Online Appendix B for further references and discussion.

[Page 6]
as Eloundou et al. (2024); Felten et al. (2023); Gmyrek et al. (2023); Handa et al. (2025), and
Tomlinson et al. (2025) adapted this approach for Generative AI, forming the basis for exposure
metrics used in this analysis. While these studies identify potential disruption, our paper connects
these exposure measures to actual employment changes.

Our work broadens insights from studies that find significant effects in more specific settings,
such as on online freelance platforms (Hui et al., 2023; Demirci et al., 2025) or within individual
firms (Brynjolfsson et al., 2025; Dillon et al., 2025).⁶ We measure labor market changes across
occupations spanning the US economy.

In this sense our work complements a small but growing list of papers using economy-wide data
to measure AI's impact. Recent findings have been varied. Jiang et al. (2025) find AI exposure
correlates with longer work hours in the U.S.⁷ Hampole et al. (2025) use job postings and LinkedIn
profiles from Revelio labs from 2011 to 2023 to find limited employment impacts overall, with
growing labor demand at firms offsetting relative declines in demand for exposed occupations.
Chandar (2025b) uses data from the CPS to compare employment changes in more and less AI-
exposed professions, finding little differential trend overall but noting difficulty with measuring
changes for young workers given limited effective sample size.⁸ Johnston and Makridis (2025)
find employment increases in state-industry pairs more exposed to AI using Quarterly Census of
Employment and Wages (QCEW) data.⁹ These prior papers use data lacking either sufficient
granularity or immediacy to reliably study employment changes by AI exposure and age (O'Brien,
2025).¹⁰ In contrast, this paper uses large-scale, close to real-time data to take a step towards
resolving the ongoing debate on the employment effects of AI on young workers.

After we first publicly shared our results, work by Hosseini and Lichtinger (2025) and Klein Teeselink
(2025) similarly found declines in AI-exposed entry-level employment using LinkedIn data from the

---
⁶See also Noy and Zhang (2023); Peng et al. (2023); Dell'Acqua et al. (2023).  
⁷See also Acemoglu et al. (2022); Bonney et al. (2024); Bick et al. (2024); Hartley et al. (2025); Frank et al. (2025);
Chen et al. (2025).  
⁸See Dominski and Lee (2025); Gimbel et al. (2025); Eckhardt and Goldschlag (2025), which also use CPS data.  
⁹Johnston and Makridis (2025) measure state-industry exposure by taking an average of Eloundou et al. (2024)'s
occupational exposure weighted by state-industry employment. Industry-level labor market changes may be distinct
from the occupation-level changes studied in this paper if firms make capital investments or become more productive
in ways that increases overall labor demand (Hampole et al., 2025).  
¹⁰As a comparison, the CPS surveyed between 44,000 and 51,000 employed individuals in total across all age groups
in each month since 2021. Between 10,000 and 12,000 of these observations were in the outgoing rotation group and
included earnings records. The data in our main analysis sample includes between 250,000 and 350,000 employed
individuals in each month just between the ages of 22 and 25, all with earnings records.

[Page 7]
US and UK. In contrast, the most recent version of Humlum and Vestergaard (2025) found minimal
effects on entry-level earnings or hours worked in Denmark.¹¹

## 3 Data Description
### 3.1 Payroll Data
This study uses data from ADP, the largest payroll processing firm in America. The company
provides payroll services for firms employing over 25 million workers in the US. We use this to
track employment changes for workers in occupations measured as more or less exposed to artificial
intelligence.

We make several restrictions for our main analysis sample. We include only workers with
positive earnings, exclude part-time employees, and subset to people under age 70.¹²

The set of firms using payroll services changes over time as companies join or leave ADP’s
platform. We maintain a consistent set of firms by keeping only companies that have employee
earnings records for each month from January 2021 through September 2025.

ADP observes job titles for about 70% of workers in its system. We exclude workers without
a recorded job title. There are over 7,000 standardized job titles, including “Search engineer
optimization specialist," "Enterprise content management manager," and "Plant documentation
control specialist." The company’s internal research team maps each of these job titles to a 2010
Standard Occupational Classification (SOC) code, additionally using information such as the job
description, industry, location, and other relevant data. We use these estimated SOC codes to
merge our data to occupational AI exposure measures.

After these restrictions we have records on 3.5 and 5 million workers each month for our main
analysis sample, though we consider robustness to alternative analyses such as allowing for firms
to enter and leave the sample.

While the ADP data include millions of workers in each month, the distribution of firms using

---
¹¹ An important direction for future work is to reconcile differences among these recent studies, assessing the extent
they arise from differences in labor market institutions, measurement of AI adoption, statistical methodology, or
other factors.

¹² While we observe the year of birth for each worker, for privacy reasons we do not observe the exact date of birth.
We impute month of birth from the distribution of birth months in the United States using data from the Center for
Disease Control and Prevention.

[Page 8]
ADP services does not exactly match the distribution of firms across the broader US economy.
Further details on differences in firm composition can be found in Cajner et al. (2018) and ADP
Research (2025).¹³

## 3.2 Occupational AI Exposure

We use two approaches for measuring occupational exposure to AI. The first uses exposure measures
from Eloundou et al. (2024), who estimate AI exposure by O*NET task using ChatGPT validated
with human labeling. They construct occupational exposure measures by aggregating the task data
to the 2018 SOC code level. We focus on the GPT-4 based $\beta$ exposure measures from their paper.

The second approach we take uses generative AI usage data from the Anthropic Economic
Index (Handa et al., 2025). This index reports the estimated share of queries pertaining to each
O*NET task based on several million conversations with Claude, Anthropic's generative AI model.
It aggregates the data to the occupational level based on these task shares. One feature of the
Anthropic Economic Index is that for each task it reports estimates of the share of queries pertaining
to that task that are "automative,” “augmentative," or none of the above. We use this as an estimate
of whether AI usage for an occupation is primarily complementary or substitutable with labor.¹⁴

We use a 2010 SOC code to 2018 SOC code crosswalk from the BLS to merge the exposure
measures to the payroll data. Table A1 shows example occupations for each AI exposure measure.

## 3.3 Other Data

To compare employment changes for teleworkable versus non-teleworkable occupations, we use data
from Dingel and Neiman (2020). We use the Personal Consumption Expenditure index from the
BLS to compute real earnings, indexed to October 2017. We use monthly Current Population
Survey (CPS) data as a comparison for our main findings.

---
¹³ Cajner et al. (2018) find a somewhat higher share of manufacturing and services firms compared to the QCEW
using data from March 2016. They also find that ADP somewhat overrepresents firms in the Northeast. In addition,
firms using ADP tend to grow faster on average than the typical firm in the US economy.

¹⁴Handa et al. (2025) use Claude to classify conversations into six categories. Directive and Feedback Loop
conversations are considered Automative; Task Iteration, Learning, and Validation are considered Augmentative.
They also instruct the model to choose None of the above "liberally." Table A2 reproduces Table 1 from Handa et al.
(2025) and shows more details about the automation and augmentation measures.

[Page 9]
# 4 Results

## 4.1 Fact 1: Employment for young workers has declined in AI-exposed occupations

Consider software engineers and customer service agents, two occupations frequently considered to be highly exposed to generative AI tools. Media attention has raised the specter of widespread employment disruption for young software engineers (Thompson, 2025; Raman, 2025; Allen, 2025; Horowitch, 2025).

Figure 1 shows employment changes by age group for these occupations, normalized to 1 in October 2022. While the types of work and workers in each of these occupations differs in many ways, both occupations present a similar pattern: employment for the youngest workers declines considerably after 2022, while employment for other age groups continues to grow. By September 2025, employment for software developers aged 22-25 declined nearly 20% compared to its peak in late 2022. Figure A1 shows that a similar pattern holds for computer occupations and service clerks more generally.

Figure A2 shows four other professions as case studies, spanning varying levels of AI exposure according to Eloundou et al. (2024). Marketing and sales managers, in the fourth quintile of AI exposure, show a decline in employment for young workers much like the case of software and customer service, albeit with smaller magnitudes. Front-line production and operations supervisors, in quintile 3, show an increase in employment for young workers, though the growth in employment is smaller than the increase for workers over age 35.

In contrast, the trends for occupations that Eloundou et al. (2024) rated as less exposed do not fit the pattern of the more exposed occupations. Stock clerks and order fillers, in quintile 2, show no obvious difference by age. Strikingly, the series for health aides, comprising nursing aides, psychiatric aides, and home health aides, show a quite different trend from software or customer service: employment for young workers has been growing *faster* than for older workers.

Figure 2 shows these patterns hold more generally across professions. The top left plot shows a divergence in employment outcomes for more and less exposed occupations for workers aged 22-25, with more exposed occupations experiencing declining employment. For older age groups, we find

[Page 10]
much less marked differences in employment growth across AI exposure quintiles.¹⁵

## 4.2 Fact 2: Though overall employment continues to grow, employment growth for young workers has been stagnant

Overall employment in the ADP data remains robust, coinciding with a low national unemployment
rate in the post-pandemic period. However, Figure A4 suggests some leveling off in employment
growth for young workers relative to other age groups, consistent with recent discussion of a wors-
ening job market for entry-level workers (Chen, 2025; Federal Reserve Bank of New York, 2025).

Figure A5 offers insight into how these trends relate to AI exposure. For each age group,
employment growth from late 2022 to September 2025 was 5-13% for the lowest three AI exposure
quintiles, with no clear ordering in employment growth by age. In contrast, for the highest two
exposure quintiles employment for 22-25 year olds declined by 6% between late 2022 and September
2025, while employment for workers aged 35-49 grew by over 8%. These results show that declining
employment in AI-exposed jobs is driving tepid overall emplyoment growth for workers between
the ages of 22 and 25.

While these findings suggest divergent employment outcomes by AI exposure for young workers,
we caution the trends observed in these first two facts could be driven by other changes in the US
economy. Our subsequent facts evaluate the robustness of the results to alternative analyses.

## 4.3 Fact 3: Entry-level employment has declined in applications of AI that automate work, with muted changes for augmentation

AI exposure can either complement or substitute for labor. These may have very different impli-
cations for the labor market (Brynjolfsson, 2022).

To assess how employment patterns differ based on the complementarity or substitutability of
AI with labor, we use data on generative AI usage from the Anthropic Economic Index (Handa
et al., 2025). The Index provides an estimate of the share of queries that pertain to each occupation.
In addition, for each task it reports estimates of the share of queries pertaining to that task that
are "automative," "augmentative," or none of the above. We use these classifications as estimates

---
¹⁵Figure A3 shows that declining employment for young workers spans a range of occupations. Close to 70% of
occupations in the first exposure quintile see rising early career employment between October 2022 and September
2025, compared to less than half of occupations in the fifth quintile.

[Page 11] [DIGITIZATION FAILED]


[Page 12]
f indexes firms, q indexes Eloundou et al. (2024) exposure quintiles, and t indexes months, with
$t = -1$ corresponding to October 2022. The outcome variable $y_{f,q,t}$ is employment in $f,q,t$.
Equation 4.1 is a Poisson event study regression controlling for firm-quintile effects, $\alpha_{f,q}$, and firm-
time effects, $\beta_{f,t}$. The firm-time effects absorb aggregate firm shocks that impact each exposure
quintile equally. The firm-quintile effects adjust for baseline differences in hiring across quintiles
within the firm. The coefficients of interest, $\gamma_{q,t}$, measure differential changes in employment growth
across quintiles after accounting for firm-time effects and firm-quintile effects.¹⁸

We run this regression separately for each age group. For each regression, we restrict to firms
that hire at least 10 workers within the age group in every period of the sample. Further, $\Sigma_t y_{f,q,t}$
must equal at least 100 for each q, meaning that the firm must at least employ on average about 2
workers from each exposure quintile across months in the sample.¹⁹ Standard errors are clustered
by firm.

Results are in Figure 4, which plots the $\gamma_{q,t}$ coefficients for each age group. For workers aged
22-25, estimates for higher quintiles are large and statistically significant, with a 15 log point de-
cline in relative employment comparable in magnitude to the estimates in the raw data in Figure 2.
Estimates for other age groups are generally much smaller in magnitude and not statistically sig-
nificant. These findings imply that the employment trends we observe are not driven by differential
shocks to firms that employ a disproportionate share of AI-exposed young workers.

One alternative confounder that would not be controlled for with firm-time effects is that even
conditional on the firm workers with high AI exposure were excessively hired after the COVID-
19 pandemic, leading to a subsequent contraction in their hiring. To assess such alternatives we
consider various other robustness checks in Section 4.6, such as removing computer occupations
and conditioning on whether the occupation is amenable to work from home.

---
¹⁸ Because of zero counts in the outcome variable, we estimate a Poisson regression instead of an OLS regression in
logs following guidance from Chen and Roth (2024).

¹⁹ Results are not sensitive to these restrictions, though there must be at least one non-zero value in each firm-month
and each firm-quintile for observations to not get dropped in the Poisson regression.

[Page 13]
## 4.5 Fact 5: Labor market adjustments are visible in employment more than compensation

In addition to employment we observe workers' annual base compensation. We use this information to test for labor market adjustment along the compensation margin.[^20] Salary data are deflated to 2017 dollars using the PCE index.[^21]

Results for various occupations are in Figure A11. The findings indicate less divergence in compensation compared to employment across more and less exposed occupations. Figure 5 shows results by age and Eloundou et al. (2024)-based exposure quintile. We find little difference in compensation trends by age or exposure quintile.

Prior work by Autor and Thompson (2025) notes that technology that replaces inexpert tasks may reduce occupational employment but increase occupational wages; technology that replaces expert tasks may do the opposite. The sign of the wage effect depends on the overall share of tasks displaced as well as the whether these tasks are expert or inexpert. The limited changes we find for wages suggest that these effects may be offsetting, at least in the short run. Alternatively, the results could be explained by wage stickiness in the short run, consistent with recent evidence from Davis and Krolikowski (2025).

## 4.6 Fact 6: Findings are largely consistent under alternative sample constructions

We test the robustness of these results to alternative sample constructions and robustness checks.

### Excluding Technology Occupations
One possibility is that our results are explained by a general slowdown in technology hiring from 2022 to 2023 as firms recovered from the COVID-19 Pandemic.[^22] Figure A12 shows employment changes by age and exposure quintile after excluding computer occupations, corresponding to 2010 SOC codes that start with 15-1. Figure A13 shows results when excluding firms in information technology or computer systems design (NAICS codes

[^20]: Total compensation may additionally include bonuses, overtime pay, commissions, equity, tips, and other items. These may have a greater impact on overall compensation in certain professions and age groups than others.
[^21]: In contrast to the series for employment, results for compensation end in August 2025, the most recently available month for the PCE index.
[^22]: Under the Tax Cuts and Jobs Act, amendments to Internal Revenue Code §174 enacted in 2022 also disallowed companies from immediately deducting R&D expenditures, including software development costs.

[Page 14]
51 and 5415). Results are quite similar, consistent with the above case studies showing employment
changes across various occupations. Results with firm-time fixed effects in Figure 4 further show
that our findings are robust to firm- or industry-level shocks that impact general hiring trends.
These results indicate that our findings are not specific to technology roles.

**Remote Work** Figures A14 and A15 show results for occupations amenable to remote work
(telework) and those that are not, according to Dingel and Neiman (2020).<sup>23</sup> We find that, for
young workers, more exposed occupations have slower employment growth, both in teleworkable
occupations and in non-teleworkable occupations. The results for non-teleworkable occupations in
particular suggest that our findings are not driven by outsourcing or work-from-home disruptions,
at least solely.<sup>24</sup>

**Longer Sample** Figure A16 shows results when extending the balanced sample of firms to 2018.
This reduces the sample size and makes the data somewhat noisier. Nonetheless, the trends remain
largely ordered by exposure in the post-GPT era, whereas this is not the case before 2022. A concern
is that for the Eloundou et al. (2024) measures the most exposed quintile had slower employment
growth starting around 2020. This is not the case for the Anthropic exposure measures, shown
in Figures A17, A18, and A19. For these measures the most exposed groups have comparable
employment growth throughout the period before generative AI, with divergent trends afterwards.

**Changes in Education** Another possibility is that our results stem from worsening education
outcomes during the COVID-19 Pandemic, as more educated workers have greater average AΙ
exposure (Kuhfeld and Lewis, 2025).<sup>25</sup> In Figure A20 we show trends for occupations in which
greater than 70% of workers have a college degree according to the 2017 American Community
Survey (ACS).<sup>26</sup> In Figure A21 we show trends for occupations in which fewer than 30% of workers

---
<sup>23</sup>Whether an occupation is amenable to remote work is positively correlated with AI exposure. Only two telework-
able occupations fall in the lowest quintile of estimated AI exposure according to the GPT-4 β measure. Likewise
few non-teleworkable occupations fall in the highest quintile of AI exposure. For this reason in Figure A14 we pool
together the two lowest AI exposure quintiles into one group. In Figure A15 we pool together the two highest AI
exposure quintiles.
<sup>24</sup>Non-teleworkable occupations with high Al exposure include bank tellers, travel agents, and tax preparers.
<sup>25</sup>Chandar (2025a) finds that declines in average skill levels for college graduates explain a sizable share of the
slowdown in the growth of the college wage gap in recent decades.
<sup>26</sup>Not a single occupation in the first quintile of GPT-4 β based exposure measure has a college share above 35%,
so that quintile is excluded from the results in Figure A20.

[Page 15]
have a college degree.

Occupations with a high share of college graduates have declining employment overall, with muted differences between more-exposed and less-exposed occupations compared to our main results. In contrast, occupations with a low share of college graduates have rising overall employment, with the least AI-exposed occupations growing and the most exposed occupations declining in employment. Further, for lower college share occupations, the dispersion in employment outcomes is visible in higher age groups as well, with workers up to age 40 showing separation in employment trends by AI exposure. These findings suggest that deteriorating education outcomes cannot fully explain our main results. They also suggest that for non-college workers, experience may serve as less of a buffer to labor market disruption than for college workers.

## Occupational Interest Rate Exposure
While estimates with firm-time effects control for overall hiring trends within firms, another possibility is that even within firms occupations with high AI exposure have high interest rate exposure, leading to contraction in hiring. We use occupational interest rate exposure data from Zens et al. (2020) to test for the correlation between interest rate exposure and AI exposure. Figure A22 in fact finds that AI exposure and interest rate exposure are negatively correlated overall, with occupations such as construction having high interest rate exposure and low AI exposure. Figures A23 and A24 repeat our analysis separately for occupations below and above the median in interest rate exposure. Both cases are consistent with our main results, suggesting that occupational differences in interest rate exposure do not drive our results.

## Other Robustness Checks
Figures A25 and A26 show results separately for men and women. The results are similar, suggesting that diverging prospects for men and women are not driving our findings. Figure A27 shows that results are similar when we do not take a balanced sample of firms. Figure A28 shows similar results when including part-time and temporary workers.[^27]

## Comparison to CPS Data
A useful benchmark for our findings is to compare them to estimates from the monthly Current Population Survey (CPS). In Online Appendix C we perform similar analyses in the CPS, finding high levels of noise consistent with small sample sizes in fine age-

[^27]: Another possibility is that employment trends reflect Covid-19 stimulus checks distorting labor supply. However, these payments were income-conditioned, and AI-exposed occupations average higher incomes (Kochhar, 2023), making this channel unlikely in explaning our findings.

[Page 16]
occupation cells. Future work should study employment trends in other large-scale data sources
such as the American Community Survey (ACS) or data from Revelio Labs as in Hosseini and
Lichtinger (2025) and Klein Teeselink (2025).

# 5 Conclusion

We document six facts about the recent labor market effects of artificial intelligence.

* We find substantial employment declines for early-career workers in occupations most exposed
to AI, such as software development and customer support.

* While economy-wide employment continues to grow, employment growth for young workers
has been stagnant.

* Entry-level employment has declined in applications of AI that *automate* work, with muted
effects for those that *augment* it.

* After conditioning on firm-time effects, young workers experienced a 16% relative employment
decline in the most exposed occupations.

* Labor market adjustments are more visible in employment than in compensation.

* These patterns hold across various alternative analyses.

While our main estimates may be influenced by factors other than generative AI, our results
are consistent with the hypothesis that generative AI has begun to affect entry-level employment
significantly.

The adoption of new technologies typically leads to heterogeneous effects across workers, result-
ing in adjustment periods as workers reallocate from displaced forms of work to new forms with
growing labor demand (Autor et al., 2024). Past transitions such as the IT revolution ultimately led
to robust growth in employment and real wages following physical and human capital adjustments,
with some workers benefiting more than others (Bresnahan et al., 2002; Brynjolfsson et al., 2021).
Tracking employment trends on an ongoing basis will help determine if the adjustment to AI
follows a similar pattern. We will continue monitoring these outcomes to assess whether the trends

[Page 17]
documented in the paper accelerate in the future. Future work would benefit from better firm-level
AI adoption data, which would provide sharper variation for estimating plausible causal effects of
AI on employment.

[Page 18]
# References

ACEMOGLU, D. AND D. AUTOR (2011): "Skills, Tasks and Technologies: Implications for Em-
ployment and Earnings*," in *Handbook of Labor Economics*, ed. by D. Card and O. Ashenfelter,
Elsevier, vol. 4, 1043-1171. 1

ACEMOGLU, D., D. AUTOR, J. HAZELL, AND P. RESTREPO (2022): “Artificial Intelligence and
Jobs: Evidence from Online Vacancies," *Journal of Labor Economics*, 40, S293-S340, publisher:
The University of Chicago Press. 7

ADP RESEARCH (2025): “ADP National Employment Report," . 3.1

ALLEN, MIKE, J. V. (2025): “Behind the Curtain: Top AI CEO foresees white-collar bloodbath,"
*Axios*. 4.1, B

AUTOR, D., C. CHIN, A. SALOMONS, AND B. SEEGMILLER (2024): “New Frontiers: The Origins
and Content of New Work, 1940–2018*," *The Quarterly Journal of Economics*, 139, 1399–1465.
5

AUTOR, D. AND N. THOMPSON (2025): “Expertise,” Working Paper, NBER. 4.5

AUTOR, D. H. (2015): “Why Are There Still So Many Jobs? The History and Future of Workplace
Automation," *Journal of Economic Perspectives*, 29, 3-30. A22

BACON, A. (2025): “Nvidia's Jensen Huang says AI could lead to job losses ‘if the world runs out
of ideas' | CNN Business," *CNN*. B

BECKER, G. S. (1994): *Human Capital: A Theoretical and Empirical Analysis with Special Refer-
ence to Education, Third Edition*, The University of Chicago Press, backup Publisher: National
Bureau of Economic Research Type: Book. 1

BICK, A., A. BLANDIN, AND D. J. DEMING (2024): “The Rapid Adoption of Generative AI,”
Working Paper, National Bureau of Economic Research. 1, 7

BONNEY, K., C. BREAUX, C. BUFFINGTON, E. DINLERSOZ, L. FOSTER, N. GOLDSCHLAG,
J. HALTIWANGER, Z. KROFF, AND K. SAVAGE (2024): "The impact of AI on the workforce:
Tasks versus jobs?" *Economics Letters*, 244, 111971. 7

[Page 19]
BOWEN, T. (2025): “Graduating into a Slowdown: Class of 2025 Meets a Frozen Job Market," . 29

BRESNAHAN, T. F., E. BRYNJOLFSSON, AND L. M. HITT (2002): “Information Technology, Workplace Organization, and the Demand for Skilled Labor: Firm-Level Evidence*," *The Quarterly Journal of Economics*, 117, 339-376. 5

BRYNJOLFSSON, E. (2022): “The Turing Trap: The Promise and Peril of Human-Like Artificial Intelligence," *Daedalus*, 151, 272-287. 4.3

BRYNJOLFSSON, E., D. LI, AND L. RAYMOND (2025): “Generative AI at Work*," *The Quarterly Journal of Economics*, 140, 889-942. 2

BRYNJOLFSSON, E. AND T. MITCHELL (2017): “What Can Machine Learning Do? Workforce Implications,” *Science*, 358, 1530-1534. 2

BRYNJOLFSSON, E., T. MITCHELL, AND D. Rock (2018): “What Can Machines Learn, and What Does It Mean for Occupations and the Economy?" *AEA Papers and Proceedings*, 108, 43-47. 2

BRYNJOLFSSON, E., D. ROCK, AND C. SYVERSON (2021): “The Productivity J-Curve: How Intangibles Complement General Purpose Technologies," *American Economic Journal: Macroeconomics*, 13, 333-372. 5

CAJNER, T., L. CRANE, R. DECKER, A. HAMINS-PUERTOLAS, C. KURZ, AND T. RADLER (2018): “Using Payroll Processor Microdata to Measure Aggregate Labor Market Activity,” Tech. rep., The Federal Reserve Board of Governors. 3.1, 13

CHANDAR, B. (2025a): “Shifts in the Composition of College Workers: Implications for US Inequality and Labor Demand," Tech. rep., Social Science Research Network. 25

———— (2025b): "Tracking Employment in AI-Exposed Jobs," Tech. rep., Social Science Research Network. 2, C, 29

CHEN, J. AND J. ROTH (2024): “Logs with Zeros? Some Problems and Solutions*,” *The Quarterly Journal of Economics*, 139, 891-936. 18

[Page 20]
CHEN, J. L. A. T.-P. (2025): "Young Graduates Are Facing an Employment Crisis," *WSJ*, section:
Economy. 4.2

CHEN, W. X., S. SRINIVASAN, AND S. ZAKERINIA (2025): "Displacement or Complementarity?
The Labor Market Impact of Generative AI,". 7

DAVIS, S. J. AND P. M. KROLIKOWSKI (2025): “Sticky Wages on the Layoff Margin,” *American
Economic Review*, 115, 491-524. 4.5

DELL'ACQUA, F., E. MCFOWLAND III, E. R. MOLLICK, H. LIFSHITZ-ASSAF, K. KELLOGG,
S. RAJENDRAN, L. KRAYER, F. CANDELON, AND K. R. LAKHANI (2023): “Navigating the
Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge
Worker Productivity and Quality," SSRN Scholarly Paper, Social Science Research Network,
Rochester, NY. 6

DEMIRCI, O., J. HANNANE, AND X. ZHU (2025): “Who is AI replacing? The impact of generative
AI on online freelancing platforms," *Management Science*. 2

DEVON, C. (2023): “On ChatGPT's one-year anniversary, it has more than 1.7 billion users—here's
what it may do next,". 3

DILLON, E., S. JAFFE, S. PENG, AND A. CAMBON (2025): “Early Impacts of M365 Copilot,"
Tech. Rep. MSR-TR-2025-18, Microsoft. 2

DINGEL, J. I. AND B. NEIMAN (2020): “How many jobs can be done at home?” *Journal of Public
Economics*, 189, 104235. 3.3, 4.6, A14, A15

DOMINSKI, J. AND Y. S. LEE (2025): “Advancing AI Capabilities and Evolving Labor Outcomes,”
Tech. rep., arXiv, arXiv:2507.08244 [econ]. 8, C

DOSHAY, H. AND A. BANTOCK (2025): “The SignalFire State of Tech Talent Report - 2025,". 29

ECKHARDT, S. AND N. GOLDSCHLAG (2025): “AI and Jobs: The Final Word (Until the Next
One)," *Economic Innovation Group*. 8, B, C

ELOUNDOU, T., S. MANNING, P. MISHKIN, AND D. Rock (2024): “GPTs are GPTs: Labor
market impact potential of LLMs," *Science*, 384, 1306-1308, publisher: American Association

[Page 21]
for the Advancement of Science. 2, 9, 3.2, 4.1, 4.3, 4.4, 4.5, 4.6, 2, 4, 5, A2, A3, A12, A13, A14, A15, A16, A20, A21, A22, A23, A24, A25, A26, A27, A28, A32, A1

ETTENHEIM, L. E. A. K. B. |. G. B. R. (2025): “AI Is Wrecking an Already Fragile Job Market for College Graduates," WSJ, section: Tech. 28

FEDERAL RESERVE BANK OF NEW YORK (2025): “The Labor Market for Recent College Gradu- ates,". 4.2

FELTEN, E., M. RAJ, AND R. SEAMANS (2021): "Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses," *Strategic Management Journal*, 42, 2195-2217, _eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1002/smj.3286. 2

——— (2023): "How will Language Modelers like ChatGPT Affect Occupations and Industries?” Tech. rep., arXiv, arXiv:2303.01157 [econ]. 2

FELTEN, E. W., M. RAJ, AND R. SEAMANS (2018): “A Method to Link Advances in Artificial Intelligence to Occupational Abilities," *AEA Papers and Proceedings*, 108, 54-57. 2

——— (2019): "The Occupational Impact of Artificial Intelligence: Labor, Skills, and Polariza- tion," SSRN Scholarly Paper, Social Science Research Network, Rochester, NY. 2

FRANK, M. R., Y.-Y. AHN, AND E. MORO (2025): “AI exposure predicts unemployment risk: A new approach to technology-driven job loss," *PNAS Nexus*, 4, pgaf107. 7

FREY, C. B. AND M. A. OSBORNE (2017): “The future of employment: How susceptible are jobs to computerisation?” *Technological Forecasting and Social Change*, 114, 254-280. 2

FRICK, W. (2025): “AI Is Everywhere But the Jobs Data,” Bloomberg.com. 5, B

GARICANO, L. (2025): “The AI Becker problem," . 1

GARICANO, L. AND L. RAYO (2025): “DP20634 Training in the Age of AI: A Theory of Appren- ticeship Viability," CEPR Discussion Paper 20634, Paris & London. 1

GIMBEL, M., M. KINDER, J. KENDALL, AND M. LEE (2025): “Evaluating the Impact of AI on the Labor Market: Current State of Affairs | The Budget Lab at Yale," . 8

[Page 22]
GMYREK, P., J. BERG, AND D. BESCOND (2023): “Generative AI and Jobs: A Global Analysis of
Potential Effects on Job Quantity and Quality," SSRN Scholarly Paper, Social Science Research
Network, Rochester, NY. 2

HAMPOLE, M., D. PAPANIKOLAOU, L. D. SCHMIDT, AND B. SEEGMILLER (2025):“Artificial
Intelligence and the Labor Market," Working Paper, National Bureau of Economic Research. 2,
9

HANDA, K., A. TAMKIN, M. MCCAIN, S. HUANG, E. DURMUS, S. HECK, J. MUELLER, J. HONG,
S. RITCHIE, T. BELONAX, K. K. TROY, D. AMODEI, J. KAPLAN, J. CLARK, AND D. GANGULI
(2025): “Which Economic Tasks are Performed with AI? Evidence from Millions of Claude
Conversations,” Tech. rep., arXiv, arXiv:2503.04761 [cs]. 2, 3.2, 14, 4.3, 3, A6, A7, A8, A9, A10,
A17, А18, А19, A1, A2

HARTLEY, J., F. JOLEVSKI, V. MELO, AND B. MOORE (2025): “The Labor Market Effects
of Generative Artificial Intelligence," SSRN Scholarly Paper, Social Science Research Network,
Rochester, NY. 1, 7

HOOVER, A. (2025): “The AI coding apocalypse,” *Business Insider*. 28

HOROWITCH, R. (2025): “The Computer-Science Bubble Is Bursting," *The Atlantic*, section: Econ-
omy. 4.1, 28

HOSSEINI, S. M. AND G. LICHTINGER (2025): “Generative AI as Seniority-Biased Technological
Change: Evidence from U.S. Résumé and Job Posting Data,". 2, 4.6

HUI, X., O. RESHEF, AND L. ZHOU (2023):“The Short-Term Effects of Generative Artificial
Intelligence on Employment: Evidence from an Online Labor Market," SSRN Scholarly Paper,
Rochester, NY. 2

HUMLUM, A. AND E. VESTERGAARD (2025): “Large Language Models, Small Labor Market Ef-
fects," Working Paper, National Bureau of Economic Research. 2

IDE, E. (2025):“Automation, AI, and the Intergenerational Transmission of Knowledge,” *arXiv
preprint arXiv:2507.16078*. 1

[Page 23]
JAMALI, L. (2025): “Microsoft to cut up to 9,000 jobs as it invests in AI,” ВВС. В

JIANG, W., J. PARK, R. XIAO, AND S. ZHANG (2025): “AI and the Extended Workday: Produc-
tivity, Contracting Efficiency, and Distribution of Rents," SSRN Scholarly Paper, Social Science
Research Network, Rochester, NY. 2

JOHNSTON, A. AND C. MAKRIDIS (2025): “The Labor Market Effects of Generative AI: A
Difference-in-Differences Analysis of AI Exposure," SSRN Scholarly Paper, Social Science Re-
search Network, Rochester, NY. 2, 9

KLEIN TEESELINK, B. (2025): “Generative AI and Labor Market Outcomes: Evidence from the
United Kingdom,". 2, 4.6

KOCHHAR, R. (2023): “Which U.S. Workers Are More Exposed to AI on Their Jobs?" *Pew
Research Center*. 27

KUHFELD, M. AND K. LEWIS (2025): “5 years after COVID-19 hit: Test data converge on math
gains, stalled reading recovery,” *Brookings*. 4.6

LENNY RACHITSKY (2025): "State of the product job market in 2025,” *Lenny's Newsletter*, ac-
cessed: 2025-05-30. 29

LIM, S., D. STRAUSS, J. BURN-MURDOCH, AND C. MURRAY (2025): “Is AI killing graduate
jobs?" *Financial Times*. B, C, 29

MASLEJ, N., L. FATTORINI, R. PERRAULT, Y. GIL, V. PARLI, N. KARIUKI, E. CAPSTICK,
A. REUEL, E. BRYNJOLFSSON, J. ETCHEMENDY, ET AL. (2025): “Artificial intelligence index
report 2025," *arXiv preprint arXiv:2504.07139*. 1

MILMO, D. AND L. ALMEIDA (2025): ““Workforce crisis': key takeaways for graduates battling AI
in the jobs market," *The Guardian*. 28

MORRIS, C. (2025): “Anthropic CEO warns AI could eliminate half of all entry-level white-collar
jobs," *Fortune*. 1

[Page 24]
NOY, S. AND W. ZHANG (2023): “Experimental evidence on the productivity effects of generative
artificial intelligence," *Science*, 381, 187–192, publisher: American Association for the Advance-
ment of Science. 6

O'BRIEN, C. (2025): "A viral chart on recent graduate unemployment is misleading," *Agglomera-
tions*. 2, C

PATWARDHAN, T., R. DIAS, E. PROEHL, G. KIM, M. WANG, O. WATKINS, S. P. FISH-
MAN, M. ALJUBEH, P. THACKER, L. FAUCONNET, N. S. KIM, P. CHAO, S. MISERENDINO,
G. CHABOT, D. LI, M. SHARMAN, A. BARR, A. GLAESE, AND J. TWOREK (2025): “GDPval:
Evaluating AI Model Performance on Real-World Economically Valuable Tasks," *arXiv preprint*.
1

PECK, E. (2025): “AI is keeping recent college grads out of work," *Axios*. 28

PENG, S., E. KALLIAMVAKOU, P. CIHON, AND M. DEMIRER (2023): “The Impact of AI on
Developer Productivity: Evidence from GitHub Copilot," Tech. rep., arXiv, arXiv:2302.06590
[cs]. 6

RAMAN, A. (2025): “Opinion | I'm a LinkedIn Executive. I See the Bottom Rung of the Career
Ladder Breaking." *The New York Times*. 5, 4.1

ROOSE, K. (2025): “For Some Recent Graduates, the A.I. Job Apocalypse May Already Be Here,"
*The New York Times*. 5

SHERMAN, N. (2025): “Amazon boss says AI will replace jobs at tech giant," *BBC News*. B

SIMON, L. K. (2025): “Is AI responsible for the rise in entry-level unemployment?” *Revelio Labs*.
29

SMITH, N. (2025): “Stop pretending you know what AI does to the economy," . B

THE ECONOMIST (2025): “Why AI hasn't taken your job,” *The Economist*. 5, B

THOMPSON, D. (2025): “Something Alarming Is Happening to the Job Market," *The Atlantic*,
section: Economy. 5, 4.1, B

[Page 25]
TOMLINSON, K., S. JAFFE, W. WANG, S. COUNTS, AND S. SURI (2025): “Working with AI:
Measuring the Occupational Implications of Generative AI," Tech. rep., arXiv, arXiv:2507.07935
[cs]. 2

WEBB, M. (2019): “The Impact of Artificial Intelligence on the Labor Market,” SSRN Scholarly
Paper, Social Science Research Network, Rochester, NY. 2

Wu, T. (2025): “Opinion | A ‘White-Collar Blood Bath' Doesn't Have to Be Our Fate,” *The New
York Times*. 28

ZENS, G., M. BÖCK, AND T. O. ZÖRNER (2020): "The heterogeneous impact of monetary policy
on the US labor market," *Journal of Economic Dynamics and Control*, 119, 103989. 4.6, A22,
A23, A24

[Page 26]
[CHART: Two line charts stacked vertically, both titled "Headcount Over Time by Age Group (Normalized)". The top chart is for "Software Developers" and the bottom is for "Customer Service". Both charts show normalized headcount on the y-axis (from 0.8 to 1.2) and date on the x-axis (from 2021-01 to 2025-09). A vertical dashed line is drawn at approximately October 2022, where all lines converge at a normalized value of 1.0. Each chart contains six lines representing different age groups: Early Career 1 (22-25), Early Career 2 (26-30), Developing (31-34), Mid-Career 1 (35-40), Mid-Career 2 (41-49), and Senior (50+). The lines show trends in employment for these groups over time.]

Figure 1: Employment changes for software developers and customer service agents by age, normalized to 1 in October 2022.

[Page 27]
[CHART: A 3x2 grid of six line charts showing employment changes over time for different age groups.
The charts are titled:
- Top-left: Early Career 1 (22-25)
- Top-right: Early Career 2 (26-30)
- Middle-left: Developing (31-34)
- Middle-right: Mid-Career 1 (35-40)
- Bottom-left: Mid-Career 2 (41-49)
- Bottom-right: Senior (50+)
Each chart has 'Headcount' on the y-axis, ranging from 0.7 to 1.2, and 'Date' on the x-axis, ranging from 2021-01 to 2025-09. A vertical line is drawn around late 2022.
Each chart displays multiple lines representing different exposure quintiles to GPT-4. Lighter grey lines represent less exposed groups, and darker grey lines represent more exposed groups. A solid red line shows the overall trend. The legend in each chart indicates 'Less exposed', 'More exposed', and 'Overall'. Generally, the headcount trends upwards over time for all groups, with some divergence between the more and less exposed groups after the vertical line.]

Figure 2: GPT-4 $\beta$. Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Exposure quintiles are defined based on the GPT-4 $\beta$ measures. Darker lines are more exposed quintiles. The red line shows the overall trend pooling across quintiles.

27

[Page 28]
[CHART: A figure containing three line charts, labeled Panel A, B, and C.
Panel A is titled "Anthropic Usage Quintile".
Panel B is titled "Automation Quintile".
Panel C is titled "Augmentation Quintile".
Each chart plots "Headcount" on the y-axis (ranging from 0.7 to 1.2) against "Date" on the x-axis (ranging from 2021-01 to 2025-09).
A vertical line is drawn on each chart around the date 2023-01.
Each chart displays three lines: a thin red line for "Less exposed", a thick black line for "More exposed", and a thin grey line for "Overall". The lines generally show an upward trend over time, with some fluctuations.]

Figure 3: Automation and Augmentation. Employment changes by age and exposure quintile using measures from Handa et al. (2025). Panel A: *Overall usage*. Exposure quintiles are defined based on the share of queries to Claude that relate to tasks associated with an occupation. Occupations whose associated tasks all have fewer than the minimum number of queries to appear in the usage data are treated as a separate category, coded as 0. Panel B: *Automation*. Automation levels are defined based on the share of queries related to an occupation that are classified by Claude as automative in nature. Occupations whose associated tasks all have fewer than the minimum number of queries to appear in the usage data are coded as 0. Note that greater than 20% of occupations above the minimum query threshold have an estimated automation share of 0. All occupations in the first and second quintile are consequently grouped together in level 1. The remaining quintiles are coded as 2, 3 and 4. Panel C: *Augmentation*. Augmentation quintiles are defined based on the share of queries related to an occupation that are classified by Claude as augmentative.

[Page 29]
[CHART: A figure composed of six panels, (a) through (f), each representing a different age group. Panel (a) is for Age 22-25, (b) for Age 26-30, (c) for Age 31-34, (d) for Age 35-40, (e) for Age 41-49, and (f) for Age 50+. Each panel contains four line graphs, one for each of Quintiles 2, 3, 4, and 5. The graphs plot the "Coefficient Estimate" over time from 2021 to 2025. Each plot shows a data line with a shaded 95% confidence interval, generally fluctuating around the zero line. A vertical red dashed line marks a point in time in late 2022.]

Figure 4: Poisson regression event study estimates for employment changes by age and AI exposure. Estimates are all relative to occupational exposure quintile 1. Exposure quintiles use Eloundou et al. (2024) GPT-4 $\beta$ measures. Estimates control for firm-time and firm-quintile fixed effects following Equation 4.1. Shaded regions are 95% confidence intervals. Standard errors are clustered by firm.

[Page 30]
[CHART: A grid of six line charts, arranged in three rows and two columns, showing trends in annual salary over time for different age groups and levels of exposure to AI. Each chart has "Date" on the x-axis, ranging from 2021-01 to 2025-09, and "Annual Salary" on the y-axis, ranging from 0.7 to 1.2. A vertical line is drawn near the date 2023-01 on each chart. Each chart includes a legend with three lines: "Less exposed" (light grey), "More exposed" (dark grey), and "Overall" (red). The charts are titled as follows:
Top-left: "Early Career 1 (22-25)"
Top-right: "Early Career 2 (26-30)"
Middle-left: "Developing (31-34)"
Middle-right: "Mid-Career 1 (35-40)"
Bottom-left: "Mid-Career 2 (41-49)"
Bottom-right: "Senior (50+)"
In all charts, the lines for "Less exposed", "More exposed", and "Overall" are relatively flat and close to each other, hovering around an annual salary of 1.0, with slight variations over time.]

Figure 5: Annual base compensation. Changes in annual base compensation by age and exposure quintile. Exposure quintiles are defined based on the GPT-4 $\beta$ measures from Eloundou et al. (2024). Darker lines are more exposed quintiles. The red line shows the overall trend pooling across quintiles. Annual base compensation is deflated to 2017 dollars using the PCE deflator.

30

[Page 31]
# Online Appendix

## A Additional Figures and Tables

[CHART: A line chart titled 'Headcount Over Time by Age Group Computer Occupations (Normalized)'. The x-axis is 'Date' ranging from 2021-01 to 2025-09. The y-axis is normalized headcount, ranging from 0.8 to 1.2. A vertical dashed line is at approximately 2022-10. The chart shows six lines representing different age groups: Early Career 1 (22-25), Early Career 2 (26-30), Developing (31-34), Mid-Career 1 (35-40), Mid-Career 2 (41-49), and Senior (50+). All lines converge at 1.0 on the dashed line. Before this point, most lines show an upward trend. After this point, the lines diverge, with some showing a slight decline and others a slight increase.]

[CHART: A line chart titled 'Headcount Over Time by Age Group Service Clerks (Normalized)'. The x-axis is 'Date' ranging from 2021-01 to 2025-09. The y-axis is normalized headcount, ranging from 0.8 to 1.2. A vertical dashed line is at approximately 2022-10. The chart shows six lines representing different age groups: Early Career 1 (22-25), Early Career 2 (26-30), Developing (31-34), Mid-Career 1 (35-40), Mid-Career 2 (41-49), and Senior (50+). All lines converge at 1.0 on the dashed line. Before this point, most lines show an upward trend. After this point, the lines diverge, with some showing a slight decline and others a slight increase.]

Figure A1: Employment changes for computer occupations (2010 SOC codes starting with 15-1) and service clerks (starting with 43-4), normalized to 1 in October 2022.

[Page 32]
[CHART: A figure containing four line charts, labeled a, b, c, and d. Each chart plots a value on the y-axis against the date on the x-axis, from April 2021 to October 2025. A vertical dashed line is present at October 2022 in each chart. The y-axis ranges from 0.8 to 1.2. Each chart contains five or six colored lines representing different career stages.

Chart a is titled "Marketing and Sales Managers". The lines generally show an upward trend.
Chart b is titled "First-Line Production Supervisors". The lines generally show an upward trend.
Chart c is titled "Stock Clerks". The lines generally show an upward trend.
Chart d is titled "Health Aides". The lines generally show an upward trend.

Below the charts is a legend for the colored lines:
- Early Career 1 (22-25)
- Early Career 2 (26-30)
- Developing (31-34)
- Mid-Career 1 (35-40)
- Mid-Career 2 (41-49)
- Senior (50+)]

Figure A2: Employment changes for marketing and sales managers (exposure quintile 4), first-line production supervisors (exposure quintile 3), stock clerks and order fillers (exposure quintile 2), and health aides (exposure quintile 1), normalized to 1 in October 2022. Exposure quintiles are defined based on the Eloundou et al. (2024) GPT-4 β measure.

32

[Page 33]
[CHART: A bar chart titled "% of Occupations with Rising Employment". The y-axis is labeled "% of Occupations" and ranges from 0 to 70. The x-axis is labeled "GPT-4 Beta Quintile" and has categories 1, 2, 3, 4, and 5. The chart shows the percentage of occupations with rising employment for each quintile. The bar heights are approximately: Quintile 1: 68%, Quintile 2: 68%, Quintile 3: 61%, Quintile 4: 49%, Quintile 5: 48%. The general trend shows a decrease in the percentage of occupations with rising employment as the GPT-4 Beta Quintile increases.]

Figure A3: Percent of occupations with an increase in employment for 22-25 year old workers between October 2022 and September 2025. Exposure quintiles are defined based on the Eloundou et al. (2024) GPT-4 $\beta$ measure.

[Page 34]
[CHART: A line chart titled "Headcount Over Time by Age Group (Normalized)". The y-axis ranges from 0.8 to 1.2. The x-axis is "Date" and ranges from 2021-01 to 2025-09. There are six lines, each representing an age group, showing an upward trend over time. A vertical dashed line is at the date 2023-01. The legend is as follows:
- Early Career 1 (22-25)
- Early Career 2 (26-30)
- Developing (31-34)
- Mid-Career 1 (35-40)
- Mid-Career 2 (41-49)
- Senior (50+)]

Figure A4: Employment changes by age. Including all occupations.

[CHART: A bar chart titled "Growth Decomposition by Age Band". The y-axis is "Growth (%)" and ranges from -5.0 to 12.5. The x-axis is "Age Band" with categories: 22-25, 26-30, 31-34, 35-40, 41-49, 50+. For each age band, there are three bars. The legend indicates the bars represent:
- AI Exposure
- Quintiles 1-3 Only
- Quintiles 4-5 Only
- All Quintiles
The bars show varying levels of positive and negative growth across the different age bands and AI exposure quintiles.]

Figure A5: Growth in employment between October 2022 and September 2025 by age and GPT-4 $\beta$-based AI exposure group.

[Page 35]
[CHART: A figure containing six line charts arranged in a 2x3 grid. Each chart plots "Headcount" on the y-axis against "Date" on the x-axis, from 2021 to late 2025. The charts are titled by age and career stage: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". Each chart shows several lines representing different exposure quintiles, with darker lines for "More exposed" and lighter lines for "Less exposed". A red line represents the "Overall" trend. All lines generally show an upward trend in headcount over time. A vertical line is present in early 2023 on each chart.]

Figure A6: Overall Claude usage. Employment changes by age and exposure quintile using Claude usage data from Handa et al. (2025). Exposure quintiles are defined based on the share of queries to Claude that relate to tasks associated with an occupation. Darker lines are more exposed quintiles. The red line shows the overall trend pooling across quintiles. Occupations whose associated tasks all have fewer than the minimum number of queries to appear in the usage data are treated as a separate category, coded as 0.

35

[Page 36]
[CHART: A 3x2 grid of six line charts showing "Headcount" on the y-axis versus "Date" on the x-axis. Each chart represents a different career stage and age group.

**Chart Titles (from top-left to bottom-right):**
1.  **Early Career 1 (22-25)**
2.  **Early Career 2 (26-30)**
3.  **Developing (31-34)**
4.  **Mid-Career 1 (35-40)**
5.  **Mid-Career 2 (41-49)**
6.  **Senior (50+)**

**Common Elements in each chart:**
*   **Y-axis:** "Headcount", ranging from 0.7 to 1.2.
*   **X-axis:** "Date", ranging from 2021-04 to 2025-04.
*   **Lines:** Three lines are plotted in each chart, showing trends over time.
    *   A light grey line labeled "Less exposed".
    *   A dark black line labeled "More exposed".
    *   A red line labeled "Overall".
*   **General Trend:** All lines in all charts show a general upward trend in headcount from 2021 to 2025. The "More exposed" line is generally slightly above the "Less exposed" line.]

Figure A7: Automation. Employment changes by age and automation level using Claude usage data from Handa et al. (2025). Automation levels are defined based on the share of queries related to an occupation that are classified by Claude as automative in nature. Darker lines are more automative. The red line shows the overall trend pooling across automation levels. Occupations whose associated tasks all have fewer than the minimum number of queries to appear in the usage data are treated as a separate category, coded as 0. Note that greater than 20% of occupations above the minimum query threshold have an estimated automation share of 0. All occupations in the first and second quintile are consequently grouped together in level 1. The remaining quintiles are coded as 2, 3 and 4.

36

[Page 37]
[CHART: A figure containing six line charts arranged in a 3x2 grid, showing employment changes by age group. Each chart plots "Headcount" on the y-axis against "Date" on the x-axis, from 2021 to 2025. The charts are titled as follows, from top-left to bottom-right: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". Each chart contains multiple lines representing different exposure quintiles, with a legend indicating "Less exposed", "More exposed", and "Overall". The "Overall" trend is a red line, while the quintiles are shown in shades of grey and black. All charts show a general upward trend in headcount over time.]

Figure A8: Augmentation. Employment changes by age and augmentation quintile using Claude usage data from Handa et al. (2025). Augmentation quintiles are defined based on the share of queries related to an occupation that are classified by Claude as augmentative. Darker lines are more augmentative quintiles. The red line shows the overall trend pooling across quintiles. Occupations whose associated tasks all have fewer than the minimum number of queries to appear in the usage data are treated as a separate category, coded as 0.

37

[Page 38]
[CHART: A 3x2 grid of six line charts showing employment changes by age and automation level. Each chart is titled with an age group: 'Early Career 1 (22-25)', 'Early Career 2 (26-30)', 'Developing (31-34)', 'Mid-Career 1 (35-40)', 'Mid-Career 2 (41-49)', and 'Senior (50+)'. The y-axis of each chart is labeled 'Headcount' and ranges from 0.7 to 1.2. The x-axis is labeled 'Date' and ranges from 2021-01 to 2025-09. Each chart contains three lines with confidence intervals: 'Less exposed' (black), 'More exposed' (red), and 'Overall' (grey). A vertical line marks the date 2023-01 on each chart. The lines generally show an upward trend in headcount over time for all groups.]

Figure A9: Employment changes by age and automation level using Claude usage data from Handa et al. (2025). Excluding occupations that have no Claude usage or are in the lowest quintile of overall Claude usage conditional on some usage.

38

[Page 39]
[CHART: A grid of six line charts, arranged in three rows and two columns, showing employment changes by age group. Each chart plots "Headcount" on the y-axis against "Date" on the x-axis, from 2021 to 2025. A vertical line marks the date 2023-01. Each chart contains three lines representing "Less exposed", "More exposed", and "Overall" employment trends. The charts are titled as follows: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". In all charts, the headcount shows a general upward trend over time for all three groups.]

Figure A10: Employment changes by age and augmentation quintile using Claude usage data from Handa et al. (2025). Excluding occupations that have no Claude usage or are in the lowest quintile of overall Claude usage conditional on some usage.

[Page 40]
[CHART: A figure composed of four line charts, labeled a, b, c, and d. Each chart plots changes in annual base compensation over time, from April 2021 to April 2025. The y-axis on all charts ranges from 0.8 to 1.2. The x-axis is labeled "Date". A vertical dashed line is present at October 2022 on all charts. Each chart contains multiple lines representing different age/career stages.
Chart a is titled "Software Developers".
Chart b is titled "Marketing and Sales Managers".
Chart c is titled "First-Line Production Supervisors".
Chart d is titled "Health Aides".]

Early Career 1 (22-25)
Early Career 2 (26-30)
Developing (31-34)
Mid-Career 1 (35-40)
Mid-Career 2 (41-49)
Senior (50+)

Figure A11: Changes in annual base compensation by age and occupation. Annual base compensation is deflated to 2017 dollars using the PCE deflator.

[Page 41]
[CHART: A 3x2 grid of six line charts, each showing "Headcount" on the y-axis versus "Date" on the x-axis. The y-axis ranges from 0.7 to 1.2, and the x-axis ranges from 2021-01 to 2025-09. Each chart corresponds to a different age group and shows three trend lines: "Less exposed" (black), "More exposed" (red), and "Overall" (grey). A vertical line is drawn around the date 2023-01. The charts are titled as follows, from top-left to bottom-right: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". In all charts, the headcount generally trends upwards. After early 2023, the growth for the "More exposed" group appears to slow down relative to the "Less exposed" group.]

Figure A12: Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Excluding computer occupations (2010 SOC codes starting with 15-1).

41

[Page 42]
[CHART: A 3x2 grid of six line charts showing employment changes by age group. Each chart plots "Headcount" on the y-axis versus "Date" on the x-axis, from 2021 to 2025. The charts are titled by age group: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". Each chart displays three trend lines with confidence intervals: "Less exposed" (black), "More exposed" (red), and "Overall" (grey), showing a general increase in headcount over time. A vertical line is drawn around the beginning of 2023.]

Figure A13: Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Excluding firms in the information sector (NAICS code 51).

[Page 43]
[CHART: A figure containing six line charts arranged in a 3x2 grid. Each chart shows "Headcount" on the y-axis versus "Date" on the x-axis from 2021 to 2025. The charts are titled by age group: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". Each chart displays three trend lines: "Less exposed" (black), "More exposed" (black), and "Overall" (red), showing changes in employment over time for different exposure groups. A vertical line marks the beginning of 2023 in each chart.]

Figure A14: Employment changes by age and exposure group using measures from Eloundou et al. (2024). Including only teleworkable occupations according to Dingel and Neiman (2020). Note that very few teleworkable occupations fall in the lowest exposure quintile. All occupations in the first and second quintile are consequently grouped together in level 1. The remaining quintiles are coded as 2, 3, and 4.

43

[Page 44]
[CHART: A 3x2 grid of six line charts showing employment changes over time for different age and career groups. Each chart plots "Headcount" on the y-axis against "Date" on the x-axis, from 2021 to late 2025. The charts are titled as follows, from top-left to bottom-right: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". Each chart contains three lines representing different exposure groups: "Less exposed" (solid black line), "More exposed" (patterned black line), and "Overall" (solid red line). A vertical line is drawn at the beginning of 2023 on each chart. Generally, all lines show an upward trend in headcount, with some divergence between the "Less exposed" and "More exposed" groups after early 2023.]

Figure A15: Employment changes by age and exposure group using measures from Eloundou et al. (2024). Including only non-teleworkable occupations according to Dingel and Neiman (2020). Note that very few non-teleworkable occupations fall in the highest exposure quintile. All occupations in the fourth and fifth quintile are consequently grouped together in level 4. The remaining quintiles are coded as 1, 2, and 3.

[Page 45]
[CHART: A 3x2 grid of six line charts showing employment changes over time for different age groups and exposure levels. Each chart is titled with a career stage and age range: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". All charts have a Y-axis labeled "Headcount" ranging from 0.7 to 1.2, and an X-axis labeled "Date" ranging from 2017-09 to 2026-01. Each chart contains three lines representing different exposure quintiles: "Less exposed" (black), "More exposed" (red), and "Overall" (grey). A vertical line is drawn on each chart around early 2022. Generally, headcount trends upwards for all groups, with the trend being steeper for younger age groups and flatter for the "Senior (50+)" group. In all charts, the "More exposed" group shows a lower headcount trend line compared to the "Less exposed" group.]

Figure A16: Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Data is from 2018 to 2025.

[Page 46]
[CHART: A 3x2 grid of six line charts, each showing employment changes by age and exposure quintile. Each chart has "Headcount" on the y-axis (from 0.7 to 1.2) and "Date" on the x-axis (from 2017-09 to 2026-01). A vertical black line is drawn around late 2022. Each chart contains three sets of lines: "Less exposed" (thin grey lines), "More exposed" (thin grey lines), and "Overall" (a solid red line). The titles of the six charts are: Top-left: "Early Career 1 (22-25)"; Top-right: "Early Career 2 (26-30)"; Middle-left: "Developing (31-34)"; Middle-right: "Mid-Career 1 (35-40)"; Bottom-left: "Mid-Career 2 (41-49)"; Bottom-right: "Senior (50+)". In all charts, the headcount generally trends upwards over time, with a noticeable dip around 2020. After the vertical line, the growth rates of the different exposure groups appear to diverge in some age categories.]

Figure A17: Employment changes by age and exposure quintile using Claude usage data from Handa et al. (2025). Occupations whose associated tasks all have fewer than the minimum number of queries to appear in the usage data are treated as a separate category, coded as 0. Data is from 2018 to 2025.

46

[Page 47]
[CHART: A 3x2 grid of six line charts showing employment changes over time, broken down by age group and automation exposure level. The charts are titled: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". Each chart plots "Headcount" on the y-axis against "Date" on the x-axis, from 2017 to 2026. Three lines are plotted on each chart: "Less exposed" (black), "More exposed" (red), and "Overall" (thicker black). The "Less exposed" and "More exposed" lines have confidence bands. A vertical line marks a point in late 2022 on each chart. Generally, headcount trends upwards for all groups, with some divergence between the "More exposed" and "Less exposed" groups after the vertical line.]

Figure A18: Employment changes by age and automation level using Claude usage data from Handa et al. (2025). Data is from 2018 to 2025.

[Page 48]
[CHART: A figure containing six line charts arranged in a 3x2 grid. Each chart shows "Headcount" on the y-axis versus "Date" on the x-axis, from 2018 to 2025. The charts are titled by career stage and age group: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". Each chart displays three trend lines: "Less exposed" (grey), "More exposed" (grey), and "Overall" (red). The "Less exposed" and "More exposed" lines have shaded confidence intervals. A vertical black line is present on each chart around late 2022. All charts show a general upward trend in headcount over time.]

Figure A19: Employment changes by age and augmentation quintile using Claude usage data from Handa et al. (2025). Data is from 2018 to 2025.

[Page 49]
[CHART: A 3x2 grid of six line charts showing employment changes by age and exposure quintile. Each chart plots "Headcount" on the y-axis against "Date" on the x-axis, from 2021 to 2025. The charts are titled by age group: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". Each chart displays three trend lines: "Less exposed" (light gray shaded area), "More exposed" (dark gray shaded area), and "Overall" (solid red line). A vertical line marks the beginning of 2023 on each chart.]

Figure A20: Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Considering only occupations in which at least 70% of workers have a college degree in the 2017 ACS. Note that no such occupations lie in quintile 1 of the GPT-4 β based exposure measure.

[Page 50]
[CHART: A 3x2 grid of six line charts showing employment changes over time for different age groups and exposure levels. Each chart has "Date" on the x-axis, from 2021-01 to 2025-09, and "Headcount" on the y-axis, from 0.7 to 1.2. A vertical line is drawn at the date 2023-01 in each chart. Each chart contains three lines: "Less exposed" (black), "More exposed" (red), and "Overall" (grey). The lines generally show an upward trend in headcount over time.

The charts are titled as follows:
- Top-left: "Early Career 1 (22-25)"
- Top-right: "Early Career 2 (26-30)"
- Middle-left: "Developing (31-34)"
- Middle-right: "Mid-Career 1 (35-40)"
- Bottom-left: "Mid-Career 2 (41-49)"
- Bottom-right: "Senior (50+)"
]

Figure A21: Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Considering only occupations in which at most 30% of workers have a college degree in the 2017 ACS.

50

[Page 51]
[CHART: A scatter plot titled "Correlation between Interest Exposure and GPT-4 Beta" with a subtitle "Pearson r = -0.346, p < 0.001". The x-axis is "Interest Cumulative 2Y (interest_cum2y)" and the y-axis is "GPT-4 Beta Exposure (gpt4_beta)". The plot shows a negative correlation between the two variables, with a red dashed trend line sloping downwards. A text box in the top left indicates a Pearson correlation coefficient of r = -0.346 with a p-value less than 0.001 for N = 398 occupations.]

Figure A22: Occupational AI exposure according to Eloundou et al. (2024) compared to interest rate exposure according to Zens et al. (2020). We measure interest rate exposure using the 2-year cumulative impulse response function identified via Cholesky decomposition. We use the crosswalk from Autor (2015) available on David Dorn's website to convert from 1990 occupation codes to 2010 Census codes. We then use a crosswalk to convert the 2010 Census codes to 2010 SOC codes, successfully merging to about 500 occupations.

[Page 52]
[CHART: A grid of six line charts, arranged in two columns and three rows, showing employment changes by age and AI exposure quintile. Each chart plots the "Headcount Ratio" on the y-axis (from 0.7 to 1.2) against the "Date" on the x-axis (from 2021-01 to 2025-09). A vertical line is drawn near the beginning of 2023 on each chart.

The charts are titled by age group:
- Top-left: "Early Career 1 (22-25)"
- Top-right: "Early Career 2 (26-30)"
- Middle-left: "Developing (31-34)"
- Middle-right: "Mid-Career 1 (35-40)"
- Bottom-left: "Mid-Career 2 (41-49)"
- Bottom-right: "Senior (50+)"

Each chart contains three main lines with a legend: a black line for "Less exposed", a red line for "More exposed", and a gray line for "Overall". Fainter gray lines are also visible in the background. In all charts, the headcount ratio generally trends upwards from 2021 to early 2023, after which the lines for "More exposed" (red) and "Less exposed" (black) diverge, with the "More exposed" line typically showing a slightly lower or flatter trajectory compared to the "Less exposed" line.]

Figure A23: Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Considering only occupations with below median interest rate exposure using data from Zens et al. (2020). Only a few occupations with low interest rate exposure also have low AI exposure. All occupations in the first and second quintile of AI exposure are consequently grouped together in level 1. The remaining quintiles are coded as 2, 3, and 4.

52

[Page 53]
[CHART: A figure containing six line charts arranged in a 3x2 grid. Each chart shows the "Headcount Ratio" on the y-axis (from 0.7 to 1.2) versus "Date" on the x-axis (from 2021-01 to 2025-09). A vertical line is drawn at the date 2023-01 on each chart. Each chart displays three lines: a black line for "Less exposed", a red line for "More exposed", and a grey line for "Overall". The charts are titled by age group as follows:
Top-left: "Early Career 1 (22-25)"
Top-right: "Early Career 2 (26-30)"
Middle-left: "Developing (31-34)"
Middle-right: "Mid-Career 1 (35-40)"
Bottom-left: "Mid-Career 2 (41-49)"
Bottom-right: "Senior (50+)"
In all charts, the lines show an upward trend over time, with some fluctuations. The "More exposed" (red) line generally starts lower than the "Less exposed" (black) line and shows a slightly different trajectory, often crossing or converging with the "Less exposed" line around or after the vertical line at 2023-01.]

Figure A24: Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Considering only occupations with above median interest rate exposure using data from Zens et al. (2020). Only a few occupations with high interest rate exposure also have high AI exposure. All occupations in the fourth and fifth quintile are consequently grouped together in level 4. The remaining quintiles are coded as 1, 2, and 3.

[Page 54]
[CHART: A figure containing six line charts arranged in a 3x2 grid. Each chart plots "Headcount" on the y-axis against "Date" on the x-axis. The y-axis ranges from 0.7 to 1.2, and the x-axis ranges from 2021-01 to 2025-09. A vertical line is drawn at the date 2023-01 in each chart. Each chart displays three lines: a black dotted line for "Less exposed", a red solid line for "More exposed", and a black solid line for "Overall". The titles for the six charts are:
1. Top-left: "Early Career 1 (22-25)"
2. Top-right: "Early Career 2 (26-30)"
3. Middle-left: "Developing (31-34)"
4. Middle-right: "Mid-Career 1 (35-40)"
5. Bottom-left: "Mid-Career 2 (41-49)"
6. Bottom-right: "Senior (50+)"
The lines in all charts generally show an upward trend over time.]

Figure A25: Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Considering only men.

54

[Page 55]
[CHART: A 3x2 grid of six line charts showing employment changes over time for different age groups of women. Each chart plots "Headcount" on the y-axis (from 0.7 to 1.2) against "Date" on the x-axis (from 2021-01 to 2025-09). The charts are titled by age group: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". Each chart contains three lines representing different exposure quintiles: "Less exposed" (black), "More exposed" (red), and "Overall" (gray). A vertical line marks a point in time around early 2023 on each chart.]

Figure A26: Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Considering only women.

[Page 56]
[CHART: A grid of six line charts, arranged in three rows and two columns, showing employment changes over time for different age groups and exposure levels.

Each chart has a title indicating the age group, a y-axis labeled "Headcount" ranging from 0.7 to 1.2, and an x-axis labeled "Date" ranging from 2021-04 to 2025-04. A vertical line is drawn at the date 2022-10 on each chart.

Each chart contains three main trend lines with surrounding fainter lines, likely confidence intervals. The legend in each chart indicates:
- "Less exposed" (black line)
- "More exposed" (red line)
- "Overall" (dotted line)

The titles of the six charts are:
- Top-left: "Early Career 1 (22-25)"
- Top-right: "Early Career 2 (26-30)"
- Middle-left: "Developing (31-34)"
- Middle-right: "Mid-Career 1 (35-40)"
- Bottom-left: "Mid-Career 2 (41-49)"
- Bottom-right: "Senior (50+)"

In general, across all charts, the "More exposed" (red) trend line shows a slight dip or slower growth compared to the "Less exposed" (black) trend line after the vertical line at 2022-10.]

Figure A27: Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Using the full sample of firms.

56

[Page 57]
[CHART: A 3x2 grid of six line charts showing employment headcount changes over time. Each chart represents a different age group. The x-axis on all charts is "Date" from 2021-01 to 2025-09. The y-axis is "Headcount" from 0.7 to 1.2. Each chart contains three lines: "Less exposed" (black dotted), "More exposed" (red solid), and "Overall" (grey solid). A vertical line is drawn around the beginning of 2023. The titles of the charts are: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)".]

Figure A28: Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Including part-time and temporary workers.

[Page 58]
[CHART: A line chart titled "Headcount over Time by Age Group Software Developers". The y-axis ranges from 0.6 to 1.8. The x-axis, labeled "Date", ranges from 2021-01 to 2025-01. The chart displays six fluctuating lines, each representing a different age group of software developers, as indicated by the legend: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". A vertical dashed line is present around October 2022, where all lines converge at the value 1.0.]

Figure A29: Employment changes for software developers by age, normalized to 1 in October 2022. Data come from the monthly CPS.

[Page 59]
[CHART: A line chart titled "Headcount over Time by Age Group, Customer Service Representatives". The x-axis is "Date" and ranges from 2021-01 to 2025-01. The y-axis is unlabeled but ranges from 0.7 to 1.4. The chart contains six fluctuating lines representing different age groups, as detailed in the legend. A vertical dashed line is present around October 2022. The legend lists the following age groups: Early Career 1 (22-25), Early Career 2 (26-30), Developing (31-34), Mid-Career 1 (35-40), Mid-Career 2 (41-49), and Senior (50+).]

Figure A30: Employment changes for customer service representatives by age, normalized to 1 in October 2022. Data come from the monthly CPS.

[Page 60]
[CHART: A line chart titled "Headcount over Time by Age Group Home Health Aides". The x-axis is labeled "Date" and ranges from 2021-01 to 2025-01. The y-axis is unlabeled and ranges from 0.5 to 4.0. The chart displays six fluctuating lines representing different age groups, with a legend on the right: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)". A vertical dashed line is present near the date 2022-07.]

Figure A31: Employment changes for home health aides by age, normalized to 1 in October 2022. Data come from the monthly CPS.

[Page 61]
[CHART: A figure containing a 2x3 grid of six line charts. Each chart plots "Employment" on the y-axis (from 0.7 to 1.2) against "Date" on the x-axis (from 2021-01 to 2025-07). The charts show data for different age groups, indicated by their titles. Each chart contains multiple lines: a dashed black line for "Less exposed", a solid black line for "More exposed", a solid red line for "Overall", and several faint gray lines in the background. The titles of the six charts are, from top-left to bottom-right: "Early Career 1 (22-25)", "Early Career 2 (26-30)", "Developing (31-34)", "Mid-Career 1 (35-40)", "Mid-Career 2 (41-49)", and "Senior (50+)".]

Figure A32: Employment changes by age and exposure quintile using measures from Eloundou et al. (2024). Data come from the monthly CPS.

61

[Page 62]
Table A1: Example occupations by exposure category

| Metric | Least exposed (examples) | Most exposed (examples) |
| :--- | :--- | :--- |
| Eloundou et al. (2024) <br> GPT-4 $\beta$ | <ul><li>Maintenance and Repair Workers, General</li><li>Nursing, Psychiatric, and Home Health Aides</li><li>Laborers and Freight, Stock, and Material Movers, Hand</li><li>Maids and Housekeeping Cleaners</li></ul> | <ul><li>Customer Service Representatives</li><li>Accountants and Auditors</li><li>Software Developers, Applications and Systems Software</li><li>Secretaries and Administrative Assistants</li></ul> |
| Handa et al. (2025) <br> (Overall) | <ul><li>Taxi Drivers and Chauffers</li><li>First-Line Supervisors of Production and Operating Workers</li><li>Laborers and Freight, Stock, and Material Movers, Hand</li><li>Maids and Housekeeping Cleaners</li></ul> | <ul><li>Computer Programmers</li><li>Financial Managers</li><li>Accountants and Auditors</li><li>Sales Representatives, Wholesale and Manufacturing</li></ul> |
| Handa et al. (2025) <br> (Automation) | <ul><li>Maintenance and Repair Workers, General</li><li>Managers, All Other</li><li>Nursing, Psychiatric, and Home Health Aides</li><li>Driver/Sales Workers and Truck Drivers</li></ul> | <ul><li>General and Operations Managers</li><li>Accountants and Auditors</li><li>Software Developers, Applications and Systems Software</li><li>Receptionists and Information Clerks</li></ul> |
| Handa et al. (2025) <br> (Augmentation) | <ul><li>Cooks</li><li>Welding, Soldering, and Brazing Workers</li><li>Tellers</li><li>Drafters</li></ul> | <ul><li>Chief Executives</li><li>Maintenance and Repair Workers, General</li><li>Registered Nurses</li><li>Computer and Information Systems Managers</li></ul> |

[Page 63]
| Automative Behaviors | Augmentative Behaviors |
| :--- | :--- |
| AI directly executes tasks with minimal human involvement | AI enhances human capabilities through collaboration |
| **Directive:** Complete task delegation with minimal interaction<br><br>*Illustrative Example:* “Format this technical documentation in Markdown” | **Task Iteration:** Collaborative refinement process<br><br>*Illustrative Example:* "Let's draft a marketing strategy for our new product. ... Good start, but can we add some concrete metrics?" |
| **Feedback Loop:** Task completion guided by environmental feedback<br><br>*Illustrative Example:* "Here's my Python script for data analysis ... it's giving an IndexError. Can you help fix it? ... Now I'm getting a different error..." | **Learning:** Knowledge acquisition and understanding<br><br>*Illustrative Example:* “Can you explain how neural networks work?” |
| | **Validation:** Work verification and improvement<br><br>*Illustrative Example:* "I've written this SQL query to find duplicate customer records. Can you check if my logic is correct and suggest any improvements?" |

Table A2: Table 1 from Handa et al. (2025). Handa et al. (2025) classify conversations from Claude, the LLM, into five distinct patterns across two broad categories based on how people integrate AI into their workflow.

[Page 64]
B Additional Literature
---

Numerous media articles have highlighted the potential employment effects of AI.[^28] Some work has noted that the unemployment rate for college graduates has risen above the rate for non-graduates, suggesting this as evidence of employment disruptions from AI (Thompson, 2025). Others have noted that these trends long preceded the spread of AI and have noted that publicly available data such as the Current Population Survey (CPS) show mixed evidence on employment changes in AI-exposed occupations (Lim et al., 2025; The Economist, 2025; Smith, 2025; Eckhardt and Goldschlag, 2025; Frick, 2025).[^29] A number of technology executives have also warned of potential job loss from AI (Allen, 2025; Sherman, 2025; Bacon, 2025) or laid off workers with the aim of incresing AI investments (Jamali, 2025).

C Comparison to CPS Data
---

The CPS surveys about 60,000 households nationwide each month to collect data on employment and other labor force characteristics. These data are released a few weeks after the reference month, giving close to real-time estimates of employment statistics. A number of prior analyses have used the CPS to assess how AI is impacting entry-level work (Chandar, 2025b; Dominski and Lee, 2025; Lim et al., 2025; Eckhardt and Goldschlag, 2025). We compare some of our main findings in the ADP data to estimates from the CPS.

Figures A29 through A31 show employment changes by age for software developers, customer service representatives, and home health aides by age using data from the CPS. Though there are millions of workers employed in these professions across the US, the estimates are highly volatile, with common fluctuations of 20% or greater in estimated employment month-to-month. Figure A32 shows estimated employment changes by age and exposure quintile using the CPS, also suggesting a high degree of volatility in the estimates.

---
[^28]: See Horowitch (2025); Ettenheim (2025); Peck (2025); Hoover (2025); Milmo and Almeida (2025); Wu (2025).
[^29]: Reports from industry have also shown mixed findings. Job posting platform TrueUp suggests a recent increase in postings in the tech sector (Lenny Rachitsky, 2025). On the other hand, Revelio Labs finds a decline in job postings, with the decrease steeper for entry-level workers (Simon, 2025). Indeed job posting data suggest declines in postings for new graduates but find these declines for less AI-exposed occupations as well (Lim et al., 2025). Chandar (2025b) notes that the correlation between job postings and employment has been weak over recent years. SignalFire finds steep declines in new graduate hires in the tech sector compared to pre-Pandemic levels (Doshay and Bantock, 2025), consistent with the findings in this paper. Data from Gusto also suggests a decline in new graduate hiring (Bowen, 2025).

[Page 65]
This volatility in CPS microdata reflects small sample sizes and the fact that the CPS is not
stratified to target employment statistics for these demographic-occupation subgroups. ³⁰ The sam-
ple size and sampling procedure of the CPS may therefore make it challenging to assess employment
changes by age and AI exposure with a high degree of confidence over the time horizon considered
in this paper (Chandar, 2025b; O'Brien, 2025).

Other large-scale data sources such as the American Community Survey (ACS) may offer a more
reliable comparison to the ADP data, though the ACS is released with a significant lag compared
to the data from ADP. We encourage comparison of our findings to results from other data sources
such as the ACS upon their release.³¹

---
³⁰ The CPS includes between 26 and 53 young software developers aged between 22 and 25 per month over our
sample period. It includes between 49 and 95 young customer service representatives, and between 2 and 14 young
home health aides.

³¹ The 2024 ACS 1-Year Public Use Microdata Sample is scheduled to be released on October 16, 2025.