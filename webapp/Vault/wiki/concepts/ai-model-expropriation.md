---
type: concept
aliases: [AI Model Expropriation]
summary: The risk that an attacker can reverse-engineer or replicate a trained AI model by repeatedly querying it, exposing its logic and making it vulnerable to manipulation.
tags: [ai-security, cybersecurity, machine-learning, adversarial-attack]
sourced_from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal 
---

# AI Model Expropriation

## The Vulnerability
Once an AI model is trained and deployed, its internal workings can be effectively exposed to the outside world through its predictions. Attackers can systematically query the prediction machine with diverse inputs to understand its logic and replicate its functionality. This expropriation of the AI's knowledge makes the machine more vulnerable to manipulation, as the attacker understands how to exploit its decision-making process.

## Method of Attack
The primary method for model expropriation involves querying the prediction machine many times. By observing the outputs for a wide variety of inputs, an attacker can infer the model's structure and parameters. This process essentially reverse-engineers the intelligence that was costly to train.

## Detection and Defense
Fortunately, such attacks leave a trail. A defense strategy involves monitoring for unusual patterns of queries, such as an abnormally high quantity or an unusual diversity of requests from a single source. These patterns can serve as red flags, indicating a potential expropriation attempt. Once an attack is detected, defenders can take action by blocking the attacker or, if that is not possible, preparing a backup plan to mitigate the damage if the machine is compromised.

---
*Extracted from: Prediction Machines The Simple Economics Of Artificial Intelligence By Ajay Agrawal *