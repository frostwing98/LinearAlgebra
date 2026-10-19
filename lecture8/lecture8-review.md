# Lecture 8 Midterm Review - Discussion Draft

This file is a content draft for the review portion of Lecture 8. It condenses Lectures 1-7 into a proposed sequence of review slides. Repeated topics are merged rather than repeated. After discussion, this draft can be revised, followed by a separate mock exam and a worked mock-exam walkthrough.

## Proposed Lecture 8 structure

1. **Review session** - reconnect the main definitions, computations, and theorems.
2. **Mock exam session** - students solve a short exam under exam-like conditions.
3. **Mock exam walkthrough** - solve each problem, explain the choice of method, and diagnose common mistakes.

## Source coverage

- **Lecture 1:** course introduction and policies; the midterm is closed-book. No new linear-algebra topic was introduced.
- **Lecture 2:** vectors, linear combinations, span, matrix equations, and solution sets.
- **Lecture 3:** linear independence, linear transformations, standard matrices, onto/one-to-one, kernel, and range.
- **Lecture 4:** matrix arithmetic, matrix multiplication, transpose, inverse matrices, and matrix equations.
- **Lecture 5:** the Invertible Matrix Theorem, partitioned matrices, and LU factorization.
- **Lecture 6:** determinant definitions, cofactor expansion, and determinant properties.
- **Lecture 7:** determinant applications, subspaces, bases, coordinates, dimension, rank, and nullity.

---

## Review slide 1 - The course in one picture

Most of the course so far connects to the equation

$$
A\mathbf{x}=\mathbf{b}.
$$

We have studied it from several viewpoints:

- **equations:** solve a linear system;
- **columns:** decide whether $\mathbf{b}$ is a linear combination of the columns of $A$;
- **geometry:** determine whether $\mathbf{b}$ lies in a span or range;
- **transformations:** interpret $A$ as the linear map $\mathbf{x}\mapsto A\mathbf{x}$;
- **structure:** use pivots, rank, null space, inverse, and determinant to classify the system.

**Central review question:** What does each representation tell us about existence and uniqueness of solutions?

---

## Review slide 2 - Vectors, linear combinations, and span

For $\mathbf{v}_1,\ldots,\mathbf{v}_p\in\mathbb{R}^n$, a linear combination is

$$
c_1\mathbf{v}_1+\cdots+c_p\mathbf{v}_p.
$$

Their span is the set of every possible linear combination:

$$
\operatorname{Span}\{\mathbf{v}_1,\ldots,\mathbf{v}_p\}
=\{c_1\mathbf{v}_1+\cdots+c_p\mathbf{v}_p:c_i\in\mathbb{R}\}.
$$

- One nonzero vector spans a line through the origin.
- Two nonparallel vectors in $\mathbb{R}^3$ span a plane through the origin.
- $\mathbf{b}\in\operatorname{Span}\{\mathbf{a}_1,\ldots,\mathbf{a}_n\}$ exactly when
  $x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n=\mathbf{b}$ is consistent.

**Exam skill:** Convert a span question into an augmented matrix and row reduce.

---

## Review slide 3 - Three equivalent forms of a linear system

If $A=[\mathbf{a}_1\ \cdots\ \mathbf{a}_n]$, then the following have the same solution set:

1. a system of linear equations;
2. the vector equation

   $$
   x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n=\mathbf{b};
   $$

3. the matrix equation

   $$
   A\mathbf{x}=\mathbf{b}.
   $$

Therefore,

$$
A\mathbf{x}=\mathbf{b}\text{ is consistent}
\iff
\mathbf{b}\in\operatorname{Col}A.
$$

For an $m\times n$ matrix, $A\mathbf{x}$ is defined for $\mathbf{x}\in\mathbb{R}^n$ and the result belongs to $\mathbb{R}^m$.

---

## Review slide 4 - Pivots, free variables, and solution types

Row reduction of $[A\mid\mathbf{b}]$ reveals the solution type.

- A row $[0\ \cdots\ 0\mid d]$ with $d\ne0$ means **no solution**.
- If the system is consistent and every variable is a pivot variable, there is **one solution**.
- If the system is consistent and at least one variable is free, there are **infinitely many solutions**.

For the homogeneous equation $A\mathbf{x}=\mathbf{0}$:

- the trivial solution $\mathbf{x}=\mathbf{0}$ always exists;
- a nontrivial solution exists exactly when there is a free variable.

For a consistent nonhomogeneous system,

$$
\mathbf{x}=\mathbf{p}+\mathbf{v}_h,
$$

where $\mathbf{p}$ is one particular solution of $A\mathbf{x}=\mathbf{b}$ and $\mathbf{v}_h$ is any solution of $A\mathbf{x}=\mathbf{0}$.

---

## Review slide 5 - Parametric vector form

After row reduction:

1. identify pivot and free variables;
2. assign a parameter to each free variable;
3. solve for the pivot variables;
4. write the solution as a vector;
5. separate the constant vector from the parameter vectors.

Homogeneous example pattern:

$$
\mathbf{x}=s\mathbf{v}_1+t\mathbf{v}_2.
$$

Consistent nonhomogeneous example pattern:

$$
\mathbf{x}=\mathbf{p}+s\mathbf{v}_1+t\mathbf{v}_2.
$$

**Geometric meaning:** a homogeneous solution set passes through the origin; a nonhomogeneous solution set is a translated copy of the corresponding homogeneous solution set.

---

## Review slide 6 - Linear independence

The set $\{\mathbf{v}_1,\ldots,\mathbf{v}_p\}$ is linearly independent if

$$
x_1\mathbf{v}_1+\cdots+x_p\mathbf{v}_p=\mathbf{0}
$$

has only the trivial solution. It is linearly dependent if a nontrivial solution exists.

Equivalent matrix test: put the vectors into the columns of $A$ and solve

$$
A\mathbf{x}=\mathbf{0}.
$$

Useful quick tests:

- a set containing $\mathbf{0}$ is dependent;
- one vector is independent exactly when it is nonzero;
- two vectors are dependent exactly when one is a scalar multiple of the other;
- more vectors than entries, $p>n$ in $\mathbb{R}^n$, guarantees dependence;
- a set is dependent exactly when at least one vector is a linear combination of the others.

---

## Review slide 7 - Linear transformations

A transformation $T$ is linear when, for all allowed vectors and scalars,

$$
T(\mathbf{u}+\mathbf{v})=T(\mathbf{u})+T(\mathbf{v}),
\qquad
T(c\mathbf{u})=cT(\mathbf{u}).
$$

Consequences:

$$
T(\mathbf{0})=\mathbf{0},
\qquad
T(c_1\mathbf{v}_1+\cdots+c_p\mathbf{v}_p)
=c_1T(\mathbf{v}_1)+\cdots+c_pT(\mathbf{v}_p).
$$

Every matrix transformation $T(\mathbf{x})=A\mathbf{x}$ is linear.

**Fast nonlinearity test:** if a proposed transformation does not send $\mathbf{0}$ to $\mathbf{0}$, it cannot be linear.

---

## Review slide 8 - The standard matrix of a transformation

Every linear transformation $T:\mathbb{R}^n\to\mathbb{R}^m$ has a unique standard matrix

$$
A=[T(\mathbf{e}_1)\ \cdots\ T(\mathbf{e}_n)]
$$

such that $T(\mathbf{x})=A\mathbf{x}$.

Procedure:

1. apply $T$ to each standard basis vector;
2. place the resulting vectors into the columns of $A$;
3. use $T(\mathbf{x})=A\mathbf{x}$.

Geometric transformations covered include contractions, dilations, shears, projections, and reflections.

**Composition order:** if $T_1(\mathbf{x})=A\mathbf{x}$ happens first and $T_2(\mathbf{x})=B\mathbf{x}$ happens second, then the composition has matrix $BA$.

---

## Review slide 9 - Onto, one-to-one, kernel, and range

For $T(\mathbf{x})=A\mathbf{x}$ with $A\in\mathbb{R}^{m\times n}$:

- $T$ is **onto** $\mathbb{R}^m$ iff $A\mathbf{x}=\mathbf{b}$ is consistent for every $\mathbf{b}\in\mathbb{R}^m$ iff $A$ has a pivot in every row.
- $T$ is **one-to-one** iff $A\mathbf{x}=\mathbf{0}$ has only the trivial solution iff $A$ has a pivot in every column.
- $\ker T=\operatorname{Nul}A$.
- $\operatorname{range}T=\operatorname{Col}A$.

For a square matrix, onto and one-to-one are equivalent; for a rectangular matrix, they need not be.

---

## Review slide 10 - Matrix arithmetic and dimensions

Matrices may be added only when they have the same size. Addition and scalar multiplication are entrywise.

For multiplication,

$$
A_{m\times r}B_{r\times n}=C_{m\times n}.
$$

The inner dimensions must match; the outer dimensions give the product size.

Three views of $AB$:

- each column of $AB$ is $A$ times the corresponding column of $B$;
- each entry is a row-column dot product;
- $AB$ represents applying $B$ first and then $A$.

Key laws:

$$
A(BC)=(AB)C,
$$

$$
A(B+C)=AB+AC,
\qquad
(A+B)C=AC+BC.
$$

In general, $AB\ne BA$, and $AB=0$ does not imply $A=0$ or $B=0$.

---

## Review slide 11 - Identity, transpose, and special matrices

The identity matrix satisfies

$$
I_n\mathbf{x}=\mathbf{x},
\qquad
AI=A=IA
$$

whenever the dimensions are appropriate.

The transpose swaps rows and columns:

$$
(A^T)_{ij}=A_{ji}.
$$

Important identities:

$$
(A^T)^T=A,
\qquad
(A+B)^T=A^T+B^T,
$$

$$
(cA)^T=cA^T,
\qquad
(AB)^T=B^TA^T.
$$

- $A$ is symmetric when $A^T=A$.
- $A$ is skew-symmetric when $A^T=-A$; its diagonal entries must be zero.

**Common trap:** the order reverses when transposing a product.

---

## Review slide 12 - Inverse matrices

A square matrix $A$ is invertible if there is a matrix $A^{-1}$ satisfying

$$
AA^{-1}=I=A^{-1}A.
$$

If an inverse exists, it is unique. A matrix with no inverse is singular.

Useful identities:

$$
(A^{-1})^{-1}=A,
$$

$$
(AB)^{-1}=B^{-1}A^{-1},
$$

$$
(A^T)^{-1}=(A^{-1})^T.
$$

Row-reduction algorithm:

$$
[A\mid I]\longrightarrow[I\mid A^{-1}].
$$

If the left block cannot be reduced to $I$, then $A$ is singular.

---

## Review slide 13 - Solving matrix equations

If $A$ is invertible, then

$$
A\mathbf{x}=\mathbf{b}
\quad\Longrightarrow\quad
\mathbf{x}=A^{-1}\mathbf{b}.
$$

The side of multiplication matters:

$$
AX=B \Longrightarrow X=A^{-1}B,
$$

$$
XA=B \Longrightarrow X=BA^{-1},
$$

$$
AXB=C \Longrightarrow X=A^{-1}CB^{-1}.
$$

Do not commute factors. Multiply by an inverse on the side where the matching factor appears.

For numerical computation, row reduction or factorization is usually preferable to explicitly computing $A^{-1}$.

---

## Review slide 14 - The Invertible Matrix Theorem

For a square $n\times n$ matrix $A$, the following statements are equivalent:

- $A$ is invertible;
- $A$ is row equivalent to $I_n$;
- $A$ has $n$ pivots;
- $A\mathbf{x}=\mathbf{0}$ has only the trivial solution;
- the columns of $A$ are linearly independent;
- the columns of $A$ span $\mathbb{R}^n$;
- $A\mathbf{x}=\mathbf{b}$ has a unique solution for every $\mathbf{b}\in\mathbb{R}^n$;
- $\mathbf{x}\mapsto A\mathbf{x}$ is one-to-one and onto;
- $A^T$ is invertible;
- $\operatorname{rank}A=n$;
- $\operatorname{Nul}A=\{\mathbf{0}\}$;
- $\det A\ne0$.

**Exam strategy:** establish whichever condition is easiest; all the others follow.

---

## Review slide 15 - Partitioned matrices

A partitioned matrix treats groups of entries as blocks. Block operations are valid only when the block dimensions are conformable.

For example,

$$
\begin{bmatrix}A_{11}&A_{12}\\A_{21}&A_{22}\end{bmatrix}
\begin{bmatrix}B_{11}&B_{12}\\B_{21}&B_{22}\end{bmatrix}
=
\begin{bmatrix}
A_{11}B_{11}+A_{12}B_{21} & A_{11}B_{12}+A_{12}B_{22}\\
A_{21}B_{11}+A_{22}B_{21} & A_{21}B_{12}+A_{22}B_{22}
\end{bmatrix}.
$$

Column-row expansion:

$$
AB=\sum_{k=1}^{n}\operatorname{col}_k(A)\operatorname{row}_k(B).
$$

For an upper block-triangular matrix with invertible diagonal blocks,

$$
\begin{bmatrix}A_{11}&A_{12}\\0&A_{22}\end{bmatrix}^{-1}
=
\begin{bmatrix}
A_{11}^{-1} & -A_{11}^{-1}A_{12}A_{22}^{-1}\\
0&A_{22}^{-1}
\end{bmatrix}.
$$

---

## Review slide 16 - LU factorization

An LU factorization writes

$$
A=LU,
$$

where $L$ is unit lower triangular and $U$ is an echelon or upper-triangular matrix.

Construction used in class:

1. reduce $A$ to $U$ using row replacements, when possible;
2. record the elimination multipliers in $L$ so that the same operations reduce $L$ to $I$;
3. verify $LU=A$.

To solve $A\mathbf{x}=\mathbf{b}$:

$$
LU\mathbf{x}=\mathbf{b}.
$$

First solve $L\mathbf{y}=\mathbf{b}$ by forward substitution, then solve $U\mathbf{x}=\mathbf{y}$ by back substitution.

**Why it matters:** the same factorization can be reused for many right-hand sides.

---

## Review slide 17 - Determinants: definitions and computation

The determinant is a scalar defined only for square matrices.

For $2\times2$ matrices,

$$
\det\begin{bmatrix}a&b\\c&d\end{bmatrix}=ad-bc.
$$

Delete row $i$ and column $j$ to form $A_{ij}$. Then

$$
M_{ij}=\det A_{ij},
\qquad
C_{ij}=(-1)^{i+j}M_{ij}.
$$

Cofactor expansion may use any row or column:

$$
\det A=\sum_j a_{ij}C_{ij}
\qquad\text{or}\qquad
\det A=\sum_i a_{ij}C_{ij}.
$$

Choose a row or column with many zeros. If $A$ is triangular, then

$$
\det A=a_{11}a_{22}\cdots a_{nn}.
$$

Sarrus' rule applies only to $3\times3$ determinants.

---

## Review slide 18 - Determinants and row operations

Track each operation carefully:

| Row operation | Effect on determinant |
|---|---|
| $R_i\leftrightarrow R_j$ | multiply by $-1$ |
| $R_i\leftarrow cR_i$ | multiply by $c$ |
| $R_i\leftarrow R_i+cR_j$ | no change |

The same rules hold for column operations.

Immediate zero tests:

- a zero row or column implies $\det A=0$;
- equal rows or columns imply $\det A=0$;
- proportional rows or columns imply $\det A=0$.

**Best workflow for a dense matrix:** use row replacement to create zeros, record every swap or scaling, and finish with the product of the diagonal entries.

---

## Review slide 19 - Determinant identities and traps

For square $n\times n$ matrices,

$$
\det(AB)=\det A\det B,
$$

$$
\det(A^T)=\det A,
$$

$$
\det(cA)=c^n\det A,
$$

$$
\det(A^k)=(\det A)^k.
$$

If $A$ is invertible,

$$
\det(A^{-1})=\frac{1}{\det A}.
$$

Common false statements:

$$
\det(A+B)\ne\det A+\det B\quad\text{in general},
$$

and scaling the entire matrix by $c$ is not the same as scaling one row by $c$.

---

## Review slide 20 - Determinants, invertibility, and system classification

For a square matrix,

$$
A\text{ invertible}\iff\det A\ne0.
$$

Thus for $A\mathbf{x}=\mathbf{b}$:

- if $\det A\ne0$, there is exactly one solution for every $\mathbf{b}$;
- if $\det A=0$, the determinant alone does not distinguish between no solution and infinitely many solutions.

When $\det A=0$, compare ranks:

$$
\operatorname{rank}A=\operatorname{rank}[A\mid\mathbf{b}]<n
\Longrightarrow \text{infinitely many solutions},
$$

$$
\operatorname{rank}A<\operatorname{rank}[A\mid\mathbf{b}]
\Longrightarrow \text{no solution}.
$$

**Common trap:** $\det A=0$ means singular, not automatically inconsistent.

---

## Review slide 21 - Cramer's rule

If $A$ is an invertible $n\times n$ matrix, then the unique solution of
$A\mathbf{x}=\mathbf{b}$ is

$$
x_i=\frac{\det A_i(\mathbf{b})}{\det A},
$$

where $A_i(\mathbf{b})$ is obtained by replacing column $i$ of $A$ with $\mathbf{b}$.

Checklist:

1. confirm that $A$ is square;
2. compute $\det A$ and confirm that it is nonzero;
3. replace the correct column, not a row;
4. compute one determinant for each requested variable.

Cramer's rule is useful for small systems and exact formulas. Row reduction is usually more efficient for large or general systems.

---

## Review slide 22 - Subspaces

A subset $H\subseteq\mathbb{R}^n$ is a subspace when

1. $\mathbf{0}\in H$;
2. $\mathbf{u}+\mathbf{v}\in H$ whenever $\mathbf{u},\mathbf{v}\in H$;
3. $c\mathbf{u}\in H$ whenever $\mathbf{u}\in H$ and $c\in\mathbb{R}$.

Important examples:

- $\{\mathbf{0}\}$ and $\mathbb{R}^n$;
- every span;
- $\operatorname{Col}A$;
- $\operatorname{Nul}A$;
- every line or plane through the origin that is closed under the operations.

A line or plane not passing through the origin is not a subspace.

**Fast test:** failure to contain $\mathbf{0}$ is enough to reject a candidate immediately.

---

## Review slide 23 - Column space and null space

For $A=[\mathbf{a}_1\ \cdots\ \mathbf{a}_n]\in\mathbb{R}^{m\times n}$,

$$
\operatorname{Col}A=\operatorname{Span}\{\mathbf{a}_1,\ldots,\mathbf{a}_n\}
\subseteq\mathbb{R}^m,
$$

$$
\operatorname{Nul}A=\{\mathbf{x}\in\mathbb{R}^n:A\mathbf{x}=\mathbf{0}\}
\subseteq\mathbb{R}^n.
$$

Membership tests:

- $\mathbf{b}\in\operatorname{Col}A$ iff $A\mathbf{x}=\mathbf{b}$ is consistent;
- $\mathbf{x}\in\operatorname{Nul}A$ iff $A\mathbf{x}=\mathbf{0}$.

**Dimension warning:** for an $m\times n$ matrix, the column space lives in $\mathbb{R}^m$, while the null space lives in $\mathbb{R}^n$.

---

## Review slide 24 - Finding bases for column and null spaces

A basis is a set that is both linearly independent and spanning.

Basis for $\operatorname{Col}A$:

1. row reduce $A$;
2. locate the pivot columns in the echelon form;
3. take the corresponding columns from the **original matrix** $A$.

Basis for $\operatorname{Nul}A$:

1. solve $A\mathbf{x}=\mathbf{0}$;
2. write the solution in parametric vector form;
3. use the coefficient vector of each free parameter as a basis vector.

**Common trap:** row operations preserve dependence relations and the null space, but usually change the column space itself. Therefore, do not use the pivot columns of the reduced matrix as a basis for $\operatorname{Col}A$ unless the problem specifically concerns that reduced matrix.

---

## Review slide 25 - Coordinates and dimension

If $\beta=\{\mathbf{b}_1,\ldots,\mathbf{b}_p\}$ is a basis for $H$, every $\mathbf{x}\in H$ has a unique representation

$$
\mathbf{x}=c_1\mathbf{b}_1+\cdots+c_p\mathbf{b}_p.
$$

The coordinate vector is

$$
[\mathbf{x}]_\beta=
\begin{bmatrix}c_1\\\vdots\\c_p\end{bmatrix}.
$$

The dimension of a nonzero subspace is the number of vectors in any basis:

$$
\dim H=p.
$$

Examples:

- $\dim\mathbb{R}^n=n$;
- a line through the origin has dimension $1$;
- a plane through the origin has dimension $2$;
- $\dim\{\mathbf{0}\}=0$.

---

## Review slide 26 - Rank, nullity, and the Rank-Nullity Theorem

For an $m\times n$ matrix $A$,

$$
\operatorname{rank}A=\dim(\operatorname{Col}A)
=\text{number of pivot columns},
$$

$$
\operatorname{nullity}A=\dim(\operatorname{Nul}A)
=\text{number of free variables}.
$$

Rank-nullity:

$$
\boxed{\operatorname{rank}A+\operatorname{nullity}A=n},
$$

where $n$ is the number of columns of $A$.

Interpretation: every variable is either a pivot variable or a free variable.

For an $n\times n$ matrix,

$$
A\text{ invertible}
\iff \operatorname{rank}A=n
\iff \operatorname{nullity}A=0.
$$

---

## Review slide 27 - The master connection map

For any $m\times n$ matrix $A$:

$$
\begin{aligned}
\mathbf{b}\in\operatorname{Col}A
&\iff A\mathbf{x}=\mathbf{b}\text{ is consistent},\\
\operatorname{Nul}A=\{\mathbf{0}\}
&\iff \text{columns of }A\text{ are linearly independent},\\
\operatorname{Col}A=\mathbb{R}^m
&\iff A\mathbf{x}=\mathbf{b}\text{ is consistent for every }\mathbf{b},\\
\operatorname{rank}A
&=\dim(\operatorname{Col}A),\\
\operatorname{nullity}A
&=\dim(\operatorname{Nul}A).
\end{aligned}
$$

When $A$ is square, each of the following says the same thing:

$$
\det A\ne0,
\quad
\operatorname{rank}A=n,
\quad
\operatorname{Nul}A=\{\mathbf{0}\},
\quad
\operatorname{Col}A=\mathbb{R}^n,
\quad
A^{-1}\text{ exists}.
$$

---

## Review slide 28 - Choosing a method on the exam

| Question type | First move |
|---|---|
| Is $\mathbf{b}$ in a span or column space? | Row reduce $[A\mid\mathbf{b}]$ |
| Are columns linearly independent? | Solve $A\mathbf{x}=\mathbf{0}$ or count pivots |
| Find a null-space basis | Solve $A\mathbf{x}=\mathbf{0}$ in parametric vector form |
| Find a column-space basis | Find pivot columns; return to the original matrix |
| Is a map onto? | Look for a pivot in every row |
| Is a map one-to-one? | Look for a pivot in every column |
| Is a square matrix invertible? | Use the easiest Invertible Matrix Theorem condition |
| Compute a determinant | Exploit zeros, triangular form, or tracked elimination |
| Solve a small invertible square system | Elimination, inverse, or Cramer's rule |
| Solve repeatedly with the same $A$ | Factor $A=LU$ |

---

## Review slide 29 - High-frequency mistakes

- Confusing a matrix with its determinant.
- Forgetting that matrix multiplication is generally not commutative.
- Writing $(AB)^{-1}=A^{-1}B^{-1}$ instead of $B^{-1}A^{-1}$.
- Writing $(AB)^T=A^TB^T$ instead of $B^TA^T$.
- Assuming $\det(A+B)=\det A+\det B$.
- Forgetting the factor $c^n$ in $\det(cA)$.
- Concluding that $\det A=0$ means a system has no solution.
- Using columns of an echelon form as a basis for the original column space.
- Mixing up “pivot in every row” with “pivot in every column.”
- Forgetting to check consistency before writing a nonhomogeneous solution as $\mathbf{p}+\mathbf{v}_h$.
- Using Cramer's rule when $\det A=0$ or when $A$ is not square.
- Giving a spanning set as a basis without checking linear independence.

---

## Review slide 30 - End-of-review checkpoint

Students should be able to answer all of the following without notes:

1. How are a linear system, a vector equation, and $A\mathbf{x}=\mathbf{b}$ connected?
2. What do pivots and free variables say about existence and uniqueness?
3. How do you test linear independence, onto, and one-to-one?
4. How do you find $A^{-1}$, a column-space basis, and a null-space basis?
5. What changes a determinant under row operations?
6. Which conditions are equivalent to invertibility for a square matrix?
7. How do rank and nullity divide the variables?
8. Which method is most efficient for the problem in front of you?

---

## Mock exam blueprint for later discussion

The mock exam should sample the course connections rather than test isolated arithmetic only. A balanced first draft could contain:

1. **Row reduction and solution sets** - classify a system and write its solution in parametric vector form.
2. **Span and linear independence** - decide membership or dependence and justify using pivots.
3. **Linear transformation** - find a standard matrix and determine onto/one-to-one.
4. **Matrix operations** - multiplication, transpose, inverse, or a matrix equation with correct order.
5. **Invertibility** - use the Invertible Matrix Theorem without necessarily computing an inverse.
6. **LU factorization** - construct or use $A=LU$ for a solve.
7. **Determinants** - combine cofactor expansion or elimination with determinant properties.
8. **Subspaces and bases** - find bases for $\operatorname{Col}A$ and $\operatorname{Nul}A$, then compute rank and nullity.

## Decisions to make before producing the lecture PDF

- How much class time should be assigned to the review, mock exam, and walkthrough?
- Is the mock exam meant to match the real midterm in length and difficulty?
- Should Lecture 8 include complete worked examples, or should some examples remain as student exercises?
- Are partitioned matrices and LU factorization definitely within the midterm scope?
- Should a one-page formula/connection sheet be included at the end of the review deck?



