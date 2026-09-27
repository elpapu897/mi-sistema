-- ~/.config/nvim/init.lua
-- Setup estilo rose-pine con lazy.nvim

-- ===== Opciones base =====
vim.g.mapleader = " "
vim.g.maplocalleader = " "

local opt = vim.opt
opt.number = true
opt.relativenumber = true
opt.tabstop = 2
opt.shiftwidth = 2
opt.expandtab = true
opt.smartindent = true
opt.wrap = false
opt.termguicolors = true
opt.cursorline = true
opt.signcolumn = "yes"
opt.scrolloff = 8
opt.mouse = "a"
opt.clipboard = "unnamedplus"
opt.ignorecase = true
opt.smartcase = true
opt.splitright = true
opt.splitbelow = true
opt.updatetime = 200

-- ===== Bootstrap de lazy.nvim =====
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- ===== Plugins =====
require("lazy").setup({
  -- Tema rose-pine
  {
    "rose-pine/neovim",
    name = "rose-pine",
    priority = 1000,
    config = function()
      require("rose-pine").setup({ variant = "main", styles = { italic = false } })
      vim.cmd("colorscheme rose-pine")
    end,
  },

  -- Barra de estado
  {
    "nvim-lualine/lualine.nvim",
    dependencies = { "nvim-tree/nvim-web-devicons" },
    config = function()
      require("lualine").setup({ options = { theme = "rose-pine", globalstatus = true } })
    end,
  },

  -- Explorador de archivos
  {
    "nvim-neo-tree/neo-tree.nvim",
    branch = "v3.x",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "nvim-tree/nvim-web-devicons",
      "MunifTanjim/nui.nvim",
    },
    keys = { { "<leader>e", "<cmd>Neotree toggle<cr>", desc = "Explorador" } },
  },

  -- Buscador (telescope)
  {
    "nvim-telescope/telescope.nvim",
    branch = "0.1.x",
    dependencies = { "nvim-lua/plenary.nvim" },
    keys = {
      { "<leader>ff", "<cmd>Telescope find_files<cr>", desc = "Buscar archivos" },
      { "<leader>fg", "<cmd>Telescope live_grep<cr>", desc = "Buscar texto" },
      { "<leader>fb", "<cmd>Telescope buffers<cr>", desc = "Buffers" },
    },
  },

  -- Resaltado de sintaxis
  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    config = function()
      require("nvim-treesitter.configs").setup({
        ensure_installed = { "lua", "vim", "vimdoc", "bash", "python", "javascript", "json" },
        highlight = { enable = true },
        indent = { enable = true },
      })
    end,
  },

  -- Guías de indentación
  { "lukas-reineke/indent-blankline.nvim", main = "ibl", opts = {} },
}, {
  ui = { border = "rounded" },
  checker = { enabled = false },
})

-- ===== Atajos extra =====
vim.keymap.set("n", "<leader>w", "<cmd>w<cr>", { desc = "Guardar" })
vim.keymap.set("n", "<leader>q", "<cmd>q<cr>", { desc = "Cerrar" })
vim.keymap.set("n", "<Esc>", "<cmd>nohlsearch<cr>")
