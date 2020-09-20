# Reinforcement Learning
## State
*s(t)* is the state of the environment at time *t*.

## Action
*a(t)* is the action taken by the agent at time *t*.

## Reward
*r(t)* is a measure of the **goodness** of the state *s*.

## Policy
*π(s,a)* is a probability distribution over the actions *a* (dependent) for each state *s* (independent).

## Return
*R(π,s)* is the sum of all future (discounted) rewards *r* for a policy *π* given the initial state *s = s0*.
Note that *G* is used as the return in some notation.

## Value function
*V(π,s)* is the expected return of the applying (recursively) the policy *π* given the initial state *s = s0*.
It is a measure of the **goodness** of the policy *pi*.

## Quality
*Q(s,a)* is the reward associated with taking action *a* in state *s*.

# AC3
## Advantage
*A(V,Q,s,a)* is the difference between the actual return *Q(s,a)* and the expected return *V(s)*.
- Advantage: A = Q(s,a) - V(s)
- Advantage Estimate: A = R - V(s)

## Loss
- Value Loss: L = Σ(R - V(s))²
- Policy Loss: L = -log(π(s)) * A(s) - β*H(π)

## Entropy
*H(π)* is a measure of the uncertainty in the policy *π*.