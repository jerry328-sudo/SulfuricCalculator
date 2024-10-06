# 硫酸溶液浓度、密度、摩尔浓度和 pH 值转换算法说明

本程序用于在硫酸溶液的质量分数、密度、摩尔浓度和 pH 值之间进行转换计算。通过输入其中一个参数，程序可以计算出其他相关参数。本文档将详细说明各个计算函数的算法，并附上相应的数学公式。

## 数据加载与插值

### 1. `load_data(json_file_path)`

**功能**：从指定的 JSON 文件中加载硫酸溶液的物性数据，包括质量分数、密度和摩尔浓度。

**参数**：

- `json_file_path`：JSON 文件的路径。

**返回值**：包含物性数据的列表。

### 2. `interpolate_property(data, x_value, x_key, y_key)`

**功能**：利用一维线性插值方法，根据已知的属性值计算对应的目标属性值。

**参数**：

- `data`：包含物性数据的列表。
- `x_value`：已知的属性值（自变量）。
- `x_key`：已知属性的键名。
- `y_key`：目标属性的键名。

**返回值**：插值计算得到的目标属性值。

**算法**：

- 提取数据中的自变量数组 `x_values` 和因变量数组 `y_values`。
- 使用 SciPy 库的 `interp1d` 函数创建插值函数 `interpolator`。
- 通过 `interpolator(x_value)` 计算目标属性值。

**数学原理**：

线性插值公式：

$$
y = y_i + \frac{(x - x_i)(y_{i+1} - y_i)}{x_{i+1} - x_i}
$$

其中，$(x_i, y_i)$和$(x_{i+1}, y_{i+1})$是相邻的已知数据点。

## 属性之间的转换函数

### 1. `get_density_from_mass_fraction(data, mass_fraction)`

**功能**：根据质量分数计算密度。

**参数**：

- `mass_fraction`：质量分数（%）。

**返回值**：对应的密度（g/cm³）。

### 2. `get_molar_concentration_from_mass_fraction(data, mass_fraction)`

**功能**：根据质量分数计算摩尔浓度。

**参数**：

- `mass_fraction`：质量分数（%）。

**返回值**：对应的摩尔浓度（mol/L）。

### 3. `get_mass_fraction_from_density(data, density)`

**功能**：根据密度计算质量分数。

**参数**：

- `density`：密度（g/cm³）。

**返回值**：对应的质量分数（%）。

### 4. `get_molar_concentration_from_density(data, density)`

**功能**：根据密度计算摩尔浓度。

**参数**：

- `density`：密度（g/cm³）。

**返回值**：对应的摩尔浓度（mol/L）。

### 5. `get_mass_fraction_from_molar_concentration(data, molar_concentration)`

**功能**：根据摩尔浓度计算质量分数。

**参数**：

- `molar_concentration`：摩尔浓度（mol/L）。

**返回值**：对应的质量分数（%）。

### 6. `get_density_from_molar_concentration(data, molar_concentration)`

**功能**：根据摩尔浓度计算密度。

**参数**：

- `molar_concentration`：摩尔浓度（mol/L）。

**返回值**：对应的密度（g/cm³）。

## pH 值的计算

### 1. `calculate_ph(molar_concentration, K2=0.0102, Kw=1e-14)`

**功能**：根据硫酸的摩尔浓度计算溶液的 pH 值。

**参数**：

- `molar_concentration`：硫酸的摩尔浓度（mol/L）。
- `K2`：硫酸的第二电离常数，默认为 0.0102。
- `Kw`：水的离子积常数，默认为$1 \times 10^{-14}$。

**返回值**：计算得到的 pH 值。

**算法与数学公式**：

硫酸在水中发生两步电离：

1. **第一步电离（完全电离）**：

  $$
   \text{H}_2\text{SO}_4 \rightarrow \text{H}^+ + \text{HSO}_4^-
  $$

2. **第二步电离（部分电离）**：

  $$
   \text{HSO}_4^- \leftrightharpoons \text{H}^+ + \text{SO}_4^{2-}, \quad K_2 = 0.0102
  $$

设总硫酸浓度为$C$，则第一步电离产生的 [$\text{H}^+$] 浓度为$C$。

设第二步电离产生的 [$\text{H}^+$] 浓度为$x$，则根据电离平衡：

$$
K_2 = \frac{x \times [\text{SO}_4^{2-}]}{[\text{HSO}_4^-]} = \frac{x^2}{C - x}
$$

考虑水的自偶离：

$$
K_w = [\text{H}^+][\text{OH}^-]
$$

总的 [$\text{H}^+$] 浓度为：

$$
[\text{H}^+] = C + x
$$

代入$[\text{OH}^-] = \frac{K_w}{[\text{H}^+]}$，结合上述方程，可以得到关于$[\text{H}^+]$的三次方程：

$$
[\text{H}^+]^3 + K_2[\text{H}^+]^2 - (2CK_2 + K_w)[\text{H}^+] - K_wK_2 = 0
$$

**求解步骤**：

- 使用 numpy 的 `roots` 函数求解三次方程，得到所有根。
- 筛选出实数且大于零的根作为有效的 [$\text{H}^+$] 浓度。
- 计算 pH 值：

 $$
  \text{pH} = -\log_{10}([\text{H}^+])
 $$

### 2. `get_molar_concentration_from_ph(ph, K2=0.0102, Kw=1e-14)`

**功能**：根据 pH 值反算硫酸的摩尔浓度。

**参数**：

- `ph`：溶液的 pH 值。
- `K2`：硫酸的第二电离常数，默认为 0.0102。
- `Kw`：水的离子积常数，默认为$1 \times 10^{-14}$。

**返回值**：计算得到的硫酸摩尔浓度（mol/L）。

**算法与数学公式**：

已知 pH 值，可以计算 [$\text{H}^+$] 浓度：

$$
[\text{H}^+] = 10^{-\text{pH}}
$$

根据电离平衡和物料守恒，可得硫酸浓度$C$的表达式：

$$
C = \frac{[\text{H}^+]^3 + K_2[\text{H}^+]^2 - K_w[\text{H}^+] - K_wK_2}{[\text{H}^+]^2 + 2K_2[\text{H}^+]}
$$

**求解步骤**：

- 计算 [$\text{H}^+$] 浓度。
- 代入上述公式，计算硫酸的摩尔浓度$C$。

## 计算流程示例

根据用户输入的不同参数，程序按照以下逻辑计算：


1. **已知质量分数**：

   - 计算密度：

    $$
     \text{density} = \text{get\_density\_from\_mass\_fraction}(\text{data}, \text{mass\_fraction})
    $$

   - 计算摩尔浓度：

    $$
     \text{molar\_concentration} = \text{get\_molar\_concentration\_from\_mass\_fraction}(\text{data}, \text{mass\_fraction})
    $$

   - 计算 pH 值：

    $$
     \text{ph\_value} = \text{calculate\_ph}(\text{molar\_concentration})
    $$

2. **已知密度**：

   - 计算质量分数：

    $$
     \text{mass\_fraction} = \text{get\_mass\_fraction\_from\_density}(\text{data}, \text{density})
    $$

   - 计算摩尔浓度：

    $$
     \text{molar\_concentration} = \text{get\_molar\_concentration\_from\_density}(\text{data}, \text{density})
    $$

   - 计算 pH 值：

    $$
     \text{ph\_value} = \text{calculate\_ph}(\text{molar\_concentration})
    $$

3. **已知摩尔浓度**：

   - 计算质量分数：

    $$
     \text{mass\_fraction} = \text{get\_mass\_fraction\_from\_molar\_concentration}(\text{data}, \text{molar\_concentration})
    $$

   - 计算密度：

    $$
     \text{density} = \text{get\_density\_from\_molar\_concentration}(\text{data}, \text{molar\_concentration})
    $$

   - 计算 pH 值：

    $$
     \text{ph\_value} = \text{calculate\_ph}(\text{molar\_concentration})
    $$

4. **已知 pH 值**：

   - 计算摩尔浓度：

    $$
     \text{molar\_concentration} = \text{get\_molar\_concentration\_from\_ph}(\text{ph\_value})
    $$

   - 计算质量分数：

    $$
     \text{mass\_fraction} = \text{get\_mass\_fraction\_from\_molar\_concentration}(\text{data}, \text{molar\_concentration})
    $$

   - 计算密度：

    $$
     \text{density} = \text{get\_density\_from\_molar\_concentration}(\text{data}, \text{molar\_concentration})
    $$

## 注意事项

- **数据范围**：插值计算依赖于数据文件中的数据范围，输入值应在数据范围内以保证准确性。

- **数值解法**：在计算 pH 值和摩尔浓度时，涉及求解三次方程，程序采用数值方法求解，可能存在近似误差。

- **活动系数**：本程序未考虑离子强度对活动系数的影响，在高浓度溶液中可能导致误差。

- **水的自偶离**：在强酸溶液中，水的自偶离可以忽略，但在计算中仍然考虑了$K_w$的影响。

## 数学公式汇总

1. **线性插值**：

  $$
   y = y_i + \frac{(x - x_i)(y_{i+1} - y_i)}{x_{i+1} - x_i}
  $$

2. **硫酸第二步电离平衡常数**：

  $$
   K_2 = \frac{[\text{H}^+][\text{SO}_4^{2-}]}{[\text{HSO}_4^-]}
  $$

3. **水的离子积**：

  $$
   K_w = [\text{H}^+][\text{OH}^-]
  $$

4. **pH 值计算**：

  $$
   \text{pH} = -\log_{10}([\text{H}^+])
  $$

5. **三次方程（求 [$\text{H}^+$]）**：

  $$
   [\text{H}^+]^3 + K_2[\text{H}^+]^2 - (2CK_2 + K_w)[\text{H}^+] - K_wK_2 = 0
  $$

6. **硫酸浓度反算公式（已知 pH 求$C$）**：

  $$
   C = \frac{[\text{H}^+]^3 + K_2[\text{H}^+]^2 - K_w[\text{H}^+] - K_wK_2}{[\text{H}^+]^2 + 2K_2[\text{H}^+]}
  $$

## 结论

通过上述算法和公式，程序可以在硫酸溶液的质量分数、密度、摩尔浓度和 pH 值之间进行精确的转换计算。这对于化学实验、工业生产和教学都有重要的实用价值。