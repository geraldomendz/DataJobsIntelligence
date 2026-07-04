class Logger:

    @staticmethod
    def separator():
        print("=" * 60)

    @staticmethod
    def company(name):
        print("\n")
        Logger.separator()
        print(f"🏢 PROCESSANDO: {name.upper()}")
        Logger.separator()

    @staticmethod
    def step(number, total, message):
        print(f"\n[{number}/{total}] {message}...")

    @staticmethod
    def success(message):
        print(f"✔ {message}")

    @staticmethod
    def warning(message):
        print(f"⚠ {message}")

    @staticmethod
    def info(message):
        print(f"ℹ {message}")

    @staticmethod
    def finish_company(name, timer):
        print(f"\n✅ {name.upper()} finalizada em {timer}.")

    @staticmethod
    def pipeline_finish(empresas, vagas, tempo):
        print()
        Logger.separator()
        print("PIPELINE FINALIZADA COM SUCESSO!")
        Logger.separator()
        print(f"🏢 Empresas processadas : {empresas}")
        print(f"📄 Total de vagas       : {vagas}")
        print(f"⏱ Tempo total          : {tempo}")